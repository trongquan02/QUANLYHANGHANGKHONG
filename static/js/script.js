let searchFrom = document.querySelector(".search-from");

document.querySelector("#search-btn").onclick = () => {
    ticketCard.classList.remove("active");
    notificationsFrom.classList.remove("active");
    loginFrom.classList.remove("active");
    navbar.classList.remove('active');
    searchFrom.classList.toggle("active");
}

let ticketCard = document.querySelector(".ticket-card");

document.querySelector("#ticket-btn").onclick = () => {
    ticketCard.classList.toggle("active");
    searchFrom.classList.remove("active");
    notificationsFrom.classList.remove("active");
    loginFrom.classList.remove("active");
    navbar.classList.remove('active');
}

let notificationsFrom = document.querySelector(".notifications-from");

document.querySelector("#notifications-btn").onclick = () => {
    notificationsFrom.classList.toggle("active");
    searchFrom.classList.remove("active");
    ticketCard.classList.remove("active");
    loginFrom.classList.remove("active");
    navbar.classList.remove('active');
}

let loginFrom = document.querySelector(".login-from");

document.querySelector("#person-btn").onclick = () => {
    loginFrom.classList.toggle("active");
    searchFrom.classList.remove("active");
    ticketCard.classList.remove("active");
    notificationsFrom.classList.remove("active");
    navbar.classList.remove('active');
}

let navbar = document.querySelector(".navbar");

document.querySelector("#menu-btn").onclick = () => {
    navbar.classList.toggle("active");
    searchFrom.classList.remove("active");
    ticketCard.classList.remove("active");
    notificationsFrom.classList.remove("active");
    loginFrom.classList.remove("active");
}

window.onscroll = () => {
    searchFrom.classList.remove("active");
    ticketCard.classList.remove("active");
    notificationsFrom.classList.remove("active");
    loginFrom.classList.remove("active");
    navbar.classList.remove('active');
}


const inputSearchAll = document.querySelectorAll(".input-search");
const autoBoxAll = document.querySelectorAll(".autobox");

const inputSearch = inputSearchAll[0];
const autoBox = autoBoxAll[0];
inputSearch.onkeyup = (e) => {
    // console.log(e.target.value);
    let checkData = e.target.value;
    let dataArray = [];
    if (checkData){
        dataArray = recomentlist.filter((data)=>{
            return data.toLocaleLowerCase().startsWith(checkData.toLocaleLowerCase());
        })
        // console.log(dataArray);
        dataArray=dataArray.map((data)=>{
            return data = "<li>"+data+"</li>";
        })

        autoBox.classList.add("active");

        showAdress(dataArray);

        let liItem = autoBox.querySelectorAll("li");
        for (let i = 0; i < liItem.length;i++) {
            liItem[i].addEventListener("click", function(){
                inputSearch.value = liItem[i].innerHTML;
                autoBox.classList.remove("active");
            })
        }

    }
    else {
        autoBox.classList.remove("active");
    }
}


function showAdress (list){
    let listData;
    if (!list.length) {
        listData = "<li>"+inputSearch.value+"</li>";
    } else {
        listData = list.join('');
    }
    autoBox.innerHTML = listData;
}


const inputSearch2 = inputSearchAll[1];
const autoBox2 = autoBoxAll[1];

inputSearch2.onkeyup = (e) => {
    // console.log(e.target.value);
    let checkData = e.target.value;
    let dataArray = [];
    if (checkData){
        dataArray = recomentlist.filter((data)=>{
            return data.toLocaleLowerCase().startsWith(checkData.toLocaleLowerCase());
        })
        // console.log(dataArray);
        dataArray=dataArray.map((data)=>{
            return data = "<li>"+data+"</li>";
        })

        autoBox2.classList.add("active");

        showAdress2(dataArray);

        let liItem = autoBox2.querySelectorAll("li");
        for (let i = 0; i < liItem.length;i++) {
            liItem[i].addEventListener("click", function(){
                inputSearch2.value = liItem[i].innerHTML;
                autoBox2.classList.remove("active");
            })
        }

    }
    else {
        autoBox2.classList.remove("active");
    }
}

function showAdress2 (list){
    let listData;
    if (!list.length) {
        listData = "<li>"+inputSearch2.value+"</li>";
    } else {
        listData = list.join('');
    }
    autoBox2.innerHTML = listData;
}


let recomentlist =[
    "Hà Nội",
    "Hải Phòng",
    "Hà Tĩnh",
    "Thanh Hóa",
    "TP Hồ Chí Minh",
    "Nghệ An",
    "Phú Quốc",
    "Quảng Ngãi",
    "Quảng Trị",
    "Quảng Ninh",
    "Đà Nẵng",
    "Đà Lạt"
]

var swiper = new swiper(".tintuc-slider",{
    loop:true,
    spaceBetween:20,
    autoplay: {
        delay: 7500,
        disableOnInteraction: false,
    },
    centeredSlides: true,
    breakpoints: {
        0: {
            slidesPerView: 1,
        },

        768: {
            slidesPerView: 2,
        },
        1205: {
            slidesPerView: 3,
        },
    },
});


