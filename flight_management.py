from flask import Flask, render_template, url_for, session, request, redirect, jsonify, flash, g
from flaskext.mysql import MySQL
from werkzeug.security import check_password_hash, generate_password_hash
import functools
from datetime import datetime

app = Flask(__name__)
mysql = MySQL()


app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'quanlychuyenbay'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'

app.config.update(SECRET_KEY='dev')
mysql.init_app(app)
conn = mysql.connect()



if conn:
    cursor = conn.cursor()


def view(table_name):
    cursor.execute("select * from {}".format(table_name))
    result = cursor.fetchall()
    return result


@app.route('/')
def home_page():
    return render_template('home.html')


@app.before_request
def load_logged_in_user():
    uname = session.get('username')
    admin = session.get('admin')

    if admin is None:
        g.admin = None
    else:
        g.admin = uname

    if uname is None:
        g.uname = None
    else:
        g.uname = uname


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.uname is None:
            return redirect(url_for('login'))

        return view(**kwargs)

    return wrapped_view

def login_required_admin(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):

        if g.admin is None:
            return redirect(url_for('loginadmin'))

        return view(**kwargs)

    return wrapped_view


@app.route('/layout')
def lay_out():
    return render_template('layout.html')




@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.args.get('user_reg'):
        flash('Đăng ký tài khoản thành công!')
        # request.args.clear()

    if request.method == 'POST':

        username = str(request.form['tenDangNhap'])
        password = str(request.form['matKhau'])

        cursor.execute(
            "SELECT * FROM khachhang WHERE ten_dang_nhap = '{}'".format(
                username)
        )
        user = cursor.fetchone()

        if user is None:
            error = "Tên đăng nhập không chính xác!"
        elif not check_password_hash(user[1], password):
            error = "Mật khẩu không chính xác!"

        if error is None:
            session.clear()
            session['username'] = user[0]
            return redirect(url_for('home_page_login'))

        flash(error)

    return render_template('login.html', error=error)


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None

    if request.method == 'POST':
        username = request.form['tenDangNhap']
        passwd = request.form['matKhau']
        fullName = request.form['hoVaTen']
        email = request.form['email']
        phoneNum = request.form['sdt']
        idNum = request.form['soCM']
        birth = datetime.strptime(
            request.form['ngaySinh'],
            '%Y-%m-%d')
        checkPasswd = request.form['nhapLaiMatKhau']

        gender = request.form['gioiTinh']

        cursor.execute(
            "SELECT * FROM khachhang WHERE ten_dang_nhap = '{}' or so_dt  = '{}' or so_cm = '{}' or email = '{}'".format(
                username, phoneNum, idNum, email)
        )
        if cursor.fetchone() is not None:
            error = 'Thông tin của người dùng đã được đăng ký'

        if passwd != checkPasswd:
            error = 'Mật khẩu và xác nhận mật khẩu không khớp'

        if error is None:
            cursor.execute(
                "INSERT INTO khachhang VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
                    username,
                    generate_password_hash(passwd),
                    fullName,
                    gender,
                    birth,
                    email,
                    phoneNum,
                    idNum
                )
            )

            res = cursor.fetchall()
            conn.commit()
            flash('Đăng ký tài khoản thành công!')
        else:

            flash(error)

    return render_template('register.html', error=error)


@app.route("/user", methods=['GET', 'POST'])
@login_required
def home_page_login():
    if request.method == 'GET':
        return render_template('home_login.html')
    else:
        return 'test'


@app.route("/user_info", methods=['GET', 'POST'])
@login_required
def user_info():
    if request.args.get('success'):
        flash('Thay đổi mật khẩu thành công')

    if request.method == 'GET':
        username = session['username']
        cursor.execute(
            "SELECT * FROM khachhang WHERE ten_dang_nhap = '{}'".format(
                username)
        )

        user = cursor.fetchone()

        fullName = user[2]
        gender = user[3]
        birth = str(user[4])[:11]
        id_num = user[7]
        email = user[5]
        phoneNum = user[6]

        return render_template('info_login.html', fullName=fullName, gender=gender, birth=birth, id_num=id_num, email=email, phoneNum=phoneNum)
    else:
        return redirect(url_for('edit_info'))


@app.route("/user_info_edit", methods=['GET', 'POST'])
@login_required
def edit_info():
    if request.method == 'GET':
        return render_template('edit_info.html')
    else:
        error = None
        newPass = request.form['matKhauMoi']
        checkNewPass = request.form['nhapLaiMatKhau']

        if newPass != checkNewPass:
            error = 'Mật khẩu nhập lại không khớp'

        if error is None:

            cursor.execute(
                "UPDATE khachhang SET mat_khau='{}' where ten_dang_nhap = '{}'".format(
                    generate_password_hash(newPass),
                    session['username'],
                )
            )

            flash("Thay đổi mật khẩu thành công")
            return render_template('edit_info.html')
        else:
            flash(error)
            return render_template('edit_info.html')


@app.route("/booking", methods=['GET', 'POST'])
@login_required
def booking():
    if request.method == 'GET':
        return render_template('booking.html')
    else:
        fromPlace = str(request.form['from'])
        toPlace = str(request.form['to'])

        return redirect(url_for('showticket', fr=fromPlace, to=toPlace))


@app.route("/showticket/<fr>/<to>", methods=['GET', 'POST'])
@login_required
def showticket(fr, to):
    print(session['username'])
    cursor.execute(
        'SELECT * \
         FROM chuyenbay \
         NATURAL JOIN ve \
         WHERE chuyenbay.diemdi LIKE "{}" \
         AND chuyenbay.diemden LIKE "{}" \
         AND chuyenbay.soghetrong > 0 \
         AND ve.ma_ve NOT IN (SELECT muave.ma_ve \
                      FROM muave \
                      WHERE ten_dang_nhap LIKE "{}")'.format(fr, to, session['username']))

    flights = cursor.fetchall()

    conn.commit()

    if request.method == 'GET':
        return render_template('showticket.html', flights=flights)
    else:
        post = "Đặt vé thành công"
        flash(post)
        flight = request.form['submit_button']

        cursor.execute(
        'SELECT * FROM chuyenbay NATURAL JOIN ve \
             WHERE chuyenbay.ma_cb LIKE "%{}%";'.format(flight))
        conn.commit()

        flight_detail = cursor.fetchone()

        cursor.execute(
            'UPDATE chuyenbay SET chuyenbay.soghetrong = {} \
              WHERE chuyenbay.ma_cb LIKE "{}"'.format(int(flight_detail[5] - 1), flight_detail[0])
        )

        cursor.execute(
        'INSERT INTO muave (ten_dang_nhap, ma_ve) \
             VALUES ("{}", "{}");'.format(session['username'], flight_detail[7]))
        
        conn.commit()
        

        return render_template('showticket.html', flights=flights, post=post)

@app.route("/booked", methods=['GET', 'POST'])
@login_required
def booked():
    cursor.execute(
        'SELECT * \
        FROM chuyenbay \
        NATURAL JOIN ve \
        WHERE ve.ma_ve IN \
            (SELECT muave.ma_ve \
            FROM muave \
            WHERE muave.ten_dang_nhap LIKE "%{}%")'.format(session['username']))
    
    tickets = cursor.fetchall()

    conn.commit()


    if request.method == 'GET':
        return render_template('booked_ticket.html', flights=tickets)
    else:
        post = "Hủy vé thành công"
        flash(post)
        flight = request.form['submit_button']

        cursor.execute(
        'SELECT * FROM chuyenbay NATURAL JOIN ve \
             WHERE chuyenbay.ma_cb LIKE "%{}%";'.format(flight))
        
        flight_detail = cursor.fetchone()
        conn.commit()


        cursor.execute(
            'UPDATE chuyenbay SET chuyenbay.soghetrong = {} \
              WHERE chuyenbay.ma_cb LIKE "%{}%"'.format(int(flight_detail[5]) + 1, flight_detail[0])
        )

        conn.commit()

        cursor.execute(
            'DELETE FROM muave WHERE muave.ma_ve LIKE "{}"'.format(flight_detail[7])
        )

        conn.commit()

        return render_template('booked_ticket.html', flights=tickets, post=post)


@app.route("/logout")
@login_required
def logout():
    session.clear()
    return redirect(url_for('home_page'))

@app.route('/check_available')
@login_required
def check_available():

    cursor.execute(
        'SELECT * FROM chuyenbay NATURAL JOIN ve'
    )

    conn.commit()

    flights = cursor.fetchall()

    return render_template('checkavailable.html', flights = flights)

# Xử lý xong toàn bộ giao diện 





















@ app.route("/loginadmin",  methods=['GET', 'POST'])
def loginadmin():
    if request.method == 'POST':
        email = str(request.form['inputEmail'])
        password = request.form['pass']
        if email != "admin":
            return render_template('admin_login.html', message_email="Tài khoản không tồn tại")
        if password != "admin":
            return render_template('admin_login.html', message_pass="Email hoặc mật khẩu không đúng")
        if email == "admin" and password:
            session['admin'] = email
            print(session)
            # print(redirect(url_for('admin')))
            return redirect(url_for('admin'))
    return render_template('admin_login.html')


@ app.route("/logoutadmin", methods=['GET'])
# @login_required_admin
def logoutadmin():
    session.clear()
    return redirect(url_for('loginadmin'))



@ app.route("/admin",  methods=['GET', 'POST'])
# @login_required_admin
def admin():
    if "admin" not in session:
        return redirect(url_for("loginadmin"))
    else:    
        if request.method == 'GET':
            return render_template('admin.html')


@ app.route("/airport_view")
# @login_required_admin
def airport_view():
    if "admin" not in session:
        return redirect(url_for("loginadmin"))
    else:    
        res = view('sanbay')
        return render_template('airport_view.html', result=res)
    


@ app.route("/airport_insert", methods=['GET', 'POST'])
# @login_required_admin
def airport_insert():
    if "admin" not in session:
        return redirect(url_for("loginadmin"))
    else:    
        if request.method == 'GET':
            return render_template('airport_insert.html')
        if request.method == "POST":
            details = request.form
            maDC = details["ma_dc"]
            thanhPho = details["thanh_pho"]

            cursor.execute("SELECT * FROM 'sanbay' WHERE ma_dc = %s", (maDC))
            sanbay = cursor.fetchone()
            
            if maDC == '' or thanhPho == '':
                error = "Chưa điền thông tin"
                flash(error)
                return render_template('airline_insert.html')
            if sanbay is not None:
                error = "Mã sân bay đã tồn tại"
                flash(error)
                return render_template('airline_insert.html')
            else:
                cursor.execute("INSERT INTO `sanbay`(`ma_dc`, `thanh_pho`) VALUES (%s,%s)", 
                                (maDC,thanhPho))
                
                hanghangkhong = view("hanghangkhong")
                for hang in hanghangkhong:
                    cursor.execute("INSERT INTO `kethop`(`ma_sanbay`, `id_hangbay`) VALUES (%s, %s)",
                                   (maDC, hang[0]))
                
                conn.commit()
                error = "Nhập thành công"
                flash(error)
                return render_template('airline_insert.html')
        return render_template('admin.html')
    
    


@ app.route("/flight_view")
# @login_required_admin
def flight_view():
    if "admin" not in session:
        return redirect(url_for("loginadmin"))
    else:    
        res = view('chuyenbay')
        return render_template('flight_view.html', result=res)

# Insert
@ app.route("/flight_insert", methods=['GET', 'POST'])
# @login_required_admin
def flight_insert():
    if "admin" in session:
        if request.method == 'GET':
            return render_template('flight_insert.html')
        if request.method == "POST":
            details = request.form
            maChuyenBay = details["input_flightid"]
            tGDi = details["input_airlineid1"]
            tGDen = details["input_arrival"]
            diemDi = details["input_departure"]
            diemDen = details["input_source"]
            soGheTrong = details["input_destination"]
            iDHangBay = details["input_route"]
            giaVe = details["input_cost"]
            maVe = 'V' + maChuyenBay

            if iDHangBay == '' or maChuyenBay == '':
                error = "Chưa điền thông tin"
                flash(error)
                return render_template('flight_insert.html')
            else: 
                cursor.execute('SELECT * FROM `hanghangkhong` WHERE ma_id = %s',(iDHangBay))
                ticket = cursor.fetchone()
                
                cursor.execute('SELECT * FROM `chuyenbay` WHERE ma_cb = %s',(maChuyenBay))
                cb = cursor.fetchone()
                
                print(ticket)
                print(cb)
                if ticket is None:  
                    error = "Mã hãng bay không tồn tại"
                    flash(error)
                    return render_template('flight_insert.html')
                if cb is not None:
                    error = "Mã chuyến bay đã tồn tại"
                    flash(error)
                    return render_template('flight_insert.html')   
                else:
                    cursor.execute("INSERT INTO `chuyenbay`(`ma_cb`, `tg_di`, `tg_den`, `diemdi`, `diemden`, `soghetrong`, `id_hangbay`) VALUES (%s,%s,%s,%s,%s,%s,%s)", 
                                    (maChuyenBay, tGDi, tGDen, diemDi, diemDen, soGheTrong, iDHangBay))
                    
                    cursor.execute("INSERT INTO `ve`(`ma_ve`, `gia_ve`, `ma_cb`) VALUES (%s,%s,%s)", 
                                    (maVe, giaVe, maChuyenBay))
                    
                    conn.commit()
                    error = "Nhập thành công"
                    flash(error)
                    return render_template('flight_insert.html')
        
        return render_template('admin.html')
    else:
        return redirect(url_for("loginadmin"))


@ app.route("/airline_view")
# @login_required_admin
def airline_view():
    if "admin" not in session:
        return redirect(url_for("loginadmin"))
    else:    
        res = view('hanghangkhong')
        return render_template('airline_view.html', result=res)



@ app.route("/airline_insert", methods=['GET', 'POST'])
# @login_required_admin
def airline_insert():
    
    # sanbay = cursor.execute("SELECT * FROM sanbay")
    # print(sanbay)
    
    
    if "admin" in session:
        if request.method == 'GET':
            # print("a")
            return render_template('airline_insert.html')
        if request.method == "POST":
            details = request.form
            maID = details["ma_id"]
            tenHang = details["ten_hang"]

            cursor.execute("SELECT * FROM `hanghangkhong` WHERE ma_id = %s", (maID))
            exits = cursor.fetchall()
            
            if maID == '' or tenHang == '':
                error = "Chưa điền thông tin"
                flash(error)
                return render_template('airline_insert.html')
            if exits is not None:
                error = "Đã tồn tại hãng hàng không"
                flash(error)
                return render_template('airline_insert.html')          
            else:
                cursor.execute("INSERT INTO `hanghangkhong`(`ma_id`, `ten_hang`) VALUES (%s,%s)", 
                                (maID,tenHang))
                
                res = view('sanbay')
                for maSanBay in res:
                    cursor.execute("INSERT INTO `kethop`(`ma_sanbay`, `id_hangbay`) VALUES (%s,%s)",
                                   (maSanBay[0],maID))
                
                conn.commit()
                error = "Nhập thành công"
                flash(error)
                return render_template('airline_insert.html')
        return render_template('admin.html')
    else:
        return redirect(url_for("loginadmin"))

@ app.route("/ve_view")
# @login_required_admin
def ve_view():
    if "admin" not in session:
        return redirect(url_for("loginadmin"))
    else:    
        res = view('ve')
        return render_template('ve_view.html', result=res)


# Insert
@ app.route("/ve_insert", methods=['GET', 'POST'])
# @login_required_admin
def ve_insert():
    if "admin" in session:
        if request.method == 'GET':
            return render_template('ve_insert.html')
        if request.method == "POST":
            details = request.form
            maVe = details["ma_ve"]
            giaVe = details["gia_ve"]
            maChuyenBay = details["ma_chuyen_bay"]

            if maVe == '' or maChuyenBay == '':
                error = "Chưa điền thông tin"
                flash(error)
                return render_template('ve_insert.html')
            else: 
                cursor.execute('SELECT * FROM `chuyenbay` WHERE ma_cb = %s',(maChuyenBay))
                ticket = cursor.fetchone()
                print(ticket)
                if ticket is None:  
                    error = "Mã chuyến bay không tồn tại"
                    flash(error)
                    return render_template('ve_insert.html')
                else:
                    cursor.execute("INSERT INTO `ve`(`ma_ve`, `gia_ve`, `ma_cb`) VALUES (%s,%s,%s)", 
                                    (maVe,giaVe, maChuyenBay))
                    conn.commit()
                    error = "Nhập thành công"
                    flash(error)
                    return render_template('ve_insert.html')
                    
        return render_template('admin.html')
    else:
        return redirect(url_for("loginadmin"))

@ app.route("/users_view")
# @login_required_admin
def users_view():
    if "admin" not in session:
        return redirect(url_for("loginadmin"))
    else:    
        res = view('khachhang')
        return render_template('users_view.html', result=res)


# Insert 
@ app.route("/usere_insert", methods=['GET', 'POST'])
# @login_required_admin
def usere_insert():
    if "admin" in session:
        if request.method == 'GET':
            return render_template('users_insert.html')
        return render_template('admin.html')
    else:
        return redirect(url_for("loginadmin"))


if __name__ == '__main__':
    app.run(debug=True)
