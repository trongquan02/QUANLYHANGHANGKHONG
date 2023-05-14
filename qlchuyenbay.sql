DROP DATABASE IF EXISTS quanlychuyenbay;

CREATE DATABASE IF NOT EXISTS quanlychuyenbay CHARACTER SET 'utf8' COLLATE 'utf8_general_ci';

USE quanlychuyenbay;

CREATE TABLE IF NOT EXISTS quantrivien
(
 ten_dang_nhap VARCHAR(8),
 mat_khau VARCHAR (250),
 PRIMARY KEY (ten_dang_nhap)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS nhanvien
(
 ma_nv VARCHAR(8),
 mat_khau VARCHAR (250),
 ho_ten VARCHAR (25),
 gioi_tinh VARCHAR (3),
 so_dt VARCHAR(12),
 PRIMARY KEY (ma_nv)
)ENGINE = INNODB;


CREATE TABLE IF NOT EXISTS quyen
(
 ma_quyen VARCHAR(8),
 ten_quyen VARCHAR (50),
 PRIMARY KEY (ma_quyen)
)ENGINE = INNODB;


CREATE TABLE IF NOT EXISTS capquyen
(
 ma_quyen VARCHAR(8),
 ma_nv VARCHAR (8),
 PRIMARY KEY (ma_quyen, ma_nv)
)ENGINE = INNODB;


CREATE TABLE IF NOT EXISTS khachhang
(
 ten_dang_nhap VARCHAR(50),
 mat_khau VARCHAR (250),
 ho_ten VARCHAR (25),
 gioi_tinh VARCHAR (3),
 ngay_sinh DATETIME,
 email VARCHAR(50),
 so_dt VARCHAR(12),
 so_cm VARCHAR(12),
 PRIMARY KEY (ten_dang_nhap)
)ENGINE = INNODB;


CREATE TABLE IF NOT EXISTS ve
(
 ma_ve VARCHAR(8),
 gia_ve INT,
 ma_cb VARCHAR(8),
 PRIMARY KEY (ma_ve)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS muave
(
 ten_dang_nhap VARCHAR(50),
 ma_ve VARCHAR(8),
 PRIMARY KEY (ten_dang_nhap, ma_ve)
)ENGINE = INNODB;


CREATE TABLE IF NOT EXISTS chuyenbay
(
 ma_cb VARCHAR(8),
 tg_di DATETIME,
 tg_den DATETIME,
 diemdi VARCHAR(25),
 diemden VARCHAR(25),
 soghetrong INT,
 id_hangbay VARCHAR(8),
 PRIMARY KEY(ma_cb)
)ENGINE = INNODB;


CREATE TABLE IF NOT EXISTS hanghangkhong
(
 ma_id VARCHAR(8),
 ten_hang VARCHAR(50),
 PRIMARY KEY (ma_id)
)ENGINE = INNODB;


CREATE TABLE IF NOT EXISTS sanbay
(
 ma_dc VARCHAR(8),
 thanh_pho VARCHAR(25),
 PRIMARY KEY (ma_dc)
)ENGINE = INNODB;


CREATE TABLE IF NOT EXISTS kethop
(
 ma_sanbay VARCHAR(8),
 id_hangbay VARCHAR(8),
 PRIMARY KEY (ma_sanbay, id_hangbay)
)ENGINE = INNODB;


ALTER TABLE muave ADD CONSTRAINT nguoimua FOREIGN KEY (ten_dang_nhap) REFERENCES khachhang(ten_dang_nhap);

ALTER TABLE muave ADD CONSTRAINT vemua FOREIGN KEY (ma_ve) REFERENCES ve(ma_ve);

ALTER TABLE ve ADD CONSTRAINT cb FOREIGN KEY (ma_cb) REFERENCES chuyenbay(ma_cb);

ALTER TABLE chuyenbay ADD CONSTRAINT hk FOREIGN KEY (id_hangbay) REFERENCES hanghangkhong(ma_id);

ALTER TABLE kethop ADD CONSTRAINT sb FOREIGN KEY (ma_sanbay) REFERENCES sanbay(ma_dc);

ALTER TABLE kethop ADD CONSTRAINT hb FOREIGN KEY (id_hangbay) REFERENCES hanghangkhong(ma_id);

ALTER TABLE capquyen ADD CONSTRAINT mq FOREIGN KEY (ma_quyen) REFERENCES quyen(ma_quyen);

ALTER TABLE capquyen ADD CONSTRAINT nv FOREIGN KEY (ma_nv) REFERENCES nhanvien(ma_nv);




insert into hanghangkhong (ma_id, ten_hang) values('VA','VietNam Airlines');
insert into hanghangkhong (ma_id, ten_hang) values('VJ','Vietjet Airs');
insert into hanghangkhong (ma_id, ten_hang) values('JP','Jetstar Pacific');
insert into hanghangkhong (ma_id, ten_hang) values('AA','Apple Airlines');
insert into hanghangkhong (ma_id, ten_hang) values('BA','Bamboo Airways');



insert into sanbay (ma_dc, thanh_pho) values ('HN', 'Hà Nội');
insert into sanbay (ma_dc, thanh_pho) values ('SG', 'TP Hồ Chí Minh');
insert into sanbay (ma_dc, thanh_pho) values ('DN', 'Đà Nẵng');
insert into sanbay (ma_dc, thanh_pho) values ('HP', 'Hải Phòng');
insert into sanbay (ma_dc, thanh_pho) values ('CT', 'Cần Thơ');
insert into sanbay (ma_dc, thanh_pho) values ('TTH', 'Huế');
insert into sanbay (ma_dc, thanh_pho) values ('BG', 'Bắc Giang');
insert into sanbay (ma_dc, thanh_pho) values ('DNN', 'Đồng Nai');
insert into sanbay (ma_dc, thanh_pho) values ('VP', 'Vĩnh Phúc');
insert into sanbay (ma_dc, thanh_pho) values ('TH', 'Thanh Hóa');
insert into sanbay (ma_dc, thanh_pho) values ('NA', 'Nghệ An');




insert into kethop (ma_sanbay, id_hangbay) values('HN', 'AA');
insert into kethop (ma_sanbay, id_hangbay) values('SG', 'AA');
insert into kethop (ma_sanbay, id_hangbay) values('DN', 'AA');
insert into kethop (ma_sanbay, id_hangbay) values('HP', 'AA');
insert into kethop (ma_sanbay, id_hangbay) values('CT', 'AA');
insert into kethop (ma_sanbay, id_hangbay) values('TTH', 'AA');
insert into kethop (ma_sanbay, id_hangbay) values('BG', 'AA');
insert into kethop (ma_sanbay, id_hangbay) values('DNN', 'AA');
insert into kethop (ma_sanbay, id_hangbay) values('VP', 'AA');
insert into kethop (ma_sanbay, id_hangbay) values('TH', 'AA');
insert into kethop (ma_sanbay, id_hangbay) values('NA', 'AA');
insert into kethop (ma_sanbay, id_hangbay) values('HN', 'VJ');
insert into kethop (ma_sanbay, id_hangbay) values('SG', 'VJ');
insert into kethop (ma_sanbay, id_hangbay) values('DN', 'VJ');
insert into kethop (ma_sanbay, id_hangbay) values('HP', 'VJ');
insert into kethop (ma_sanbay, id_hangbay) values('CT', 'VJ');
insert into kethop (ma_sanbay, id_hangbay) values('TTH', 'VJ');
insert into kethop (ma_sanbay, id_hangbay) values('BG', 'VJ');
insert into kethop (ma_sanbay, id_hangbay) values('DNN', 'VJ');
insert into kethop (ma_sanbay, id_hangbay) values('VP', 'VJ');
insert into kethop (ma_sanbay, id_hangbay) values('TH', 'VJ');
insert into kethop (ma_sanbay, id_hangbay) values('NA', 'VJ');
insert into kethop (ma_sanbay, id_hangbay) values('HN', 'JP');
insert into kethop (ma_sanbay, id_hangbay) values('SG', 'JP');
insert into kethop (ma_sanbay, id_hangbay) values('DN', 'JP');
insert into kethop (ma_sanbay, id_hangbay) values('HP', 'JP');
insert into kethop (ma_sanbay, id_hangbay) values('CT', 'JP');
insert into kethop (ma_sanbay, id_hangbay) values('TTH', 'JP');
insert into kethop (ma_sanbay, id_hangbay) values('BG', 'JP');
insert into kethop (ma_sanbay, id_hangbay) values('DNN', 'JP');
insert into kethop (ma_sanbay, id_hangbay) values('VP', 'JP');
insert into kethop (ma_sanbay, id_hangbay) values('TH', 'JP');
insert into kethop (ma_sanbay, id_hangbay) values('NA', 'JP');
insert into kethop (ma_sanbay, id_hangbay) values('HN', 'VA');
insert into kethop (ma_sanbay, id_hangbay) values('SG', 'VA');
insert into kethop (ma_sanbay, id_hangbay) values('DN', 'VA');
insert into kethop (ma_sanbay, id_hangbay) values('HP', 'VA');
insert into kethop (ma_sanbay, id_hangbay) values('CT', 'VA');
insert into kethop (ma_sanbay, id_hangbay) values('TTH', 'VA');
insert into kethop (ma_sanbay, id_hangbay) values('BG', 'VA');
insert into kethop (ma_sanbay, id_hangbay) values('DNN', 'VA');
insert into kethop (ma_sanbay, id_hangbay) values('VP', 'VA');
insert into kethop (ma_sanbay, id_hangbay) values('TH', 'VA');
insert into kethop (ma_sanbay, id_hangbay) values('NA', 'VA');
insert into kethop (ma_sanbay, id_hangbay) values('HN', 'BA');
insert into kethop (ma_sanbay, id_hangbay) values('SG', 'BA');
insert into kethop (ma_sanbay, id_hangbay) values('DN', 'BA');
insert into kethop (ma_sanbay, id_hangbay) values('HP', 'BA');
insert into kethop (ma_sanbay, id_hangbay) values('CT', 'BA');
insert into kethop (ma_sanbay, id_hangbay) values('TTH', 'BA');
insert into kethop (ma_sanbay, id_hangbay) values('BG', 'BA');
insert into kethop (ma_sanbay, id_hangbay) values('DNN', 'BA');
insert into kethop (ma_sanbay, id_hangbay) values('VP', 'BA');
insert into kethop (ma_sanbay, id_hangbay) values('TH', 'BA');
insert into kethop (ma_sanbay, id_hangbay) values('NA', 'BA');



insert into chuyenbay (ma_cb, tg_di, tg_den, diemdi, diemden, soghetrong, id_hangbay) values
('VA101', '2022-12-01 10:00:00', '2022-12-01 12:00:00', 'Hà Nội', 'TP Hồ Chí Minh', 100, 'VA');
insert into chuyenbay (ma_cb, tg_di, tg_den, diemdi, diemden, soghetrong, id_hangbay) values
('VA102', '2022-12-01 07:00:00', '2022-12-01 08:20:00', 'Hà Nội', 'Đà Nẵng', 100, 'VA');
insert into chuyenbay (ma_cb, tg_di, tg_den, diemdi, diemden, soghetrong, id_hangbay) values
('VJ101', '2022-12-01 13:00:00', '2022-12-01 14:00:00', 'Hà Nội', 'Huế', 100, 'VJ');
insert into chuyenbay (ma_cb, tg_di, tg_den, diemdi, diemden, soghetrong, id_hangbay) values
('VJ102', '2022-12-01 21:00:00', '2022-12-01 22:00:00', 'Bắc Giang', 'Đà Nẵng', 100, 'VJ');
insert into chuyenbay (ma_cb, tg_di, tg_den, diemdi, diemden, soghetrong, id_hangbay) values
('JP101', '2022-12-01 10:00:00', '2022-12-01 12:00:00', 'TP Hồ Chí Minh', 'Hà Nội', 100, 'JP');
insert into chuyenbay (ma_cb, tg_di, tg_den, diemdi, diemden, soghetrong, id_hangbay) values
('JP102', '2022-12-01 07:00:00', '2022-12-01 08:45:00', 'Hà Nội', 'TP Hồ Chí Minh', 100, 'JP');
insert into chuyenbay (ma_cb, tg_di, tg_den, diemdi, diemden, soghetrong, id_hangbay) values
('AA101', '2022-12-01 15:00:00', '2022-12-01 17:00:00', 'Hà Nội', 'TP Hồ Chí Minh', 100, 'AA');
insert into chuyenbay (ma_cb, tg_di, tg_den, diemdi, diemden, soghetrong, id_hangbay) values
('AA102', '2022-12-01 19:00:00', '2022-12-01 21:10:00', 'TP Hồ Chí Minh', 'Bắc Giang', 100, 'AA');
insert into chuyenbay (ma_cb, tg_di, tg_den, diemdi, diemden, soghetrong, id_hangbay) values
('BA101', '2022-12-01 10:00:00', '2022-12-01 12:00:00', 'Hà Nội', 'Cần Thơ', 100, 'BA');
insert into chuyenbay (ma_cb, tg_di, tg_den, diemdi, diemden, soghetrong, id_hangbay) values
('BA102', '2022-12-01 16:00:00', '2022-12-01 17:00:00', 'Hà Nội', 'TP Hồ Chí Minh', 100, 'BA');
insert into chuyenbay (ma_cb, tg_di, tg_den, diemdi, diemden, soghetrong, id_hangbay) values
('BA103', '2022-12-01 16:00:00', '2022-12-01 17:00:00', 'Hải Phòng', 'TP Hồ Chí Minh', 100, 'BA');



insert into ve (ma_ve, gia_ve, ma_cb) values ('VVA101', 700000, 'VA101');
insert into ve (ma_ve, gia_ve, ma_cb) values ('VVA102', 600000, 'VA102');
insert into ve (ma_ve, gia_ve, ma_cb) values ('VVJ101', 500000, 'VJ101');
insert into ve (ma_ve, gia_ve, ma_cb) values ('VVJ102', 600000, 'VJ102');
insert into ve (ma_ve, gia_ve, ma_cb) values ('VJP101', 700000, 'JP101');
insert into ve (ma_ve, gia_ve, ma_cb) values ('VJP102', 700000, 'JP102');
insert into ve (ma_ve, gia_ve, ma_cb) values ('VAA101', 700000, 'AA101');
insert into ve (ma_ve, gia_ve, ma_cb) values ('VAA102', 750000, 'AA102');
insert into ve (ma_ve, gia_ve, ma_cb) values ('VBA101', 800000, 'BA101');
insert into ve (ma_ve, gia_ve, ma_cb) values ('VBA102', 700000, 'BA102');
insert into ve (ma_ve, gia_ve, ma_cb) values ('VBA103', 800000, 'BA103');







insert into quyen (ma_quyen, ten_quyen) values('Q1', 'Thêm sân bay');
insert into quyen (ma_quyen, ten_quyen) values('Q2', 'Thêm hãng hàng không');
insert into quyen (ma_quyen, ten_quyen) values('Q3', 'Thêm chuyến bay');
insert into quyen (ma_quyen, ten_quyen) values('Q4', 'Xóa sân bay');
insert into quyen (ma_quyen, ten_quyen) values('Q5', 'Xóa hãng hàng không');
insert into quyen (ma_quyen, ten_quyen) values('Q6', 'Xóa chuyến bay');


insert into nhanvien (ma_nv, mat_khau, ho_ten, gioi_tinh, so_dt) 
values('001', '001', 'Nguyễn Duy Anh', 'nam', '0912345');

insert into nhanvien (ma_nv, mat_khau, ho_ten, gioi_tinh, so_dt) 
values('002', '002', 'Lê Thế Cường', 'nam', '0912346');

insert into nhanvien (ma_nv, mat_khau, ho_ten, gioi_tinh, so_dt) 
values('003', '003', 'Vũ Trọng Quân', 'nam', '0912347');





