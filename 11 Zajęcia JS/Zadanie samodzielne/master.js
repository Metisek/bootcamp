let a = 0;
let licznik;
var checkLog;

let timeStart = performance.now();
let timeEnd = performance.now();

function gra(){
    checkLog = 1;
    logTime();
    var x = Math.floor(Math.random() * 256);
    var y = Math.floor(Math.random() * 256);
    var z = Math.floor(Math.random() * 256);
    var xx = Math.floor(Math.random() * 10000);
    var yy = Math.floor(Math.random() * 10000);
    var lefta = xx/100
    var topa = yy/100
    var bgColor = "rgb(" + x + "," + y + "," + z + ")";
    console.log(bgColor)
    document.getElementById('gra').innerHTML="<button id='granie' onclick='graCLick()'> </button>";
    document.getElementById('granie').style.background=bgColor;
    document.getElementById('granie').style.top=topa+"%";
    document.getElementById('granie').style.left=lefta+"%";
    timeStart = performance.now();
    a++;
};

function logTime(){
        if (checkLog == 0){
            return;
        };
        timeEnd = performance.now();
        setTimeout(logTime, 30);
            timeCount = timeEnd-timeStart;
            document.getElementById('gracz').innerHTML = "<p align='left'> Czas:"+(Math.round(timeCount)/1000).toPrecision(5)+" ms</p>";
};

function graStart(){
    licznik = document.getElementById('odliczanie').value;
    document.getElementById('clear').innerHTML = "";
    document.getElementById('gra').style.width = '98vw';
    document.getElementById('gra').style.height = '98vh';
    logTime();
    gra();
};

function graCLick(){
    document.getElementById('gra').innerHTML="";
    checkLog = 0;
    if (a < licznik){
        randomNum = Math.floor(Math.random() * (2000 - 200)) + 200;
        setTimeout(gra, randomNum);
    }
    else{
        document.getElementById('gracz').innerHTML = "";
    };
};