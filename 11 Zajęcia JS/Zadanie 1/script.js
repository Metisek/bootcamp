let data = new Date();

if (6 < data.getHours() < 18){
    document.body.style.backgroundColor = "#FF6600";
    document.getElementById('photo').src = "dzien.jpg";
}
else{
    document.body.style.backgroundColor = "#000077";
    document.body.style.color = "#FFFFFF";
    document.getElementById('photo').src = "noc.jpg";
};

