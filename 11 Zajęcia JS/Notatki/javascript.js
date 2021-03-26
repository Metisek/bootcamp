// alert('Działa');

let data = new Date();
// alert(data.getFullYear());
obj = {0:"Styczeń",
       1:"Luty",
       2:"Marzec",
       3:"Kwiecień"
};

console.log("Hello world");
console.log(obj);

// document.querySelector("#btn").addEventListener("click", () => {

// });

let myPrecious = document.getElementById('akapit').style.color;

function PokazDate(prefix) {
       alert(prefix+' '+obj[data.getMonth()] +' '+data.getFullYear());
};

let i = 0;

function zmienKolor() {
       if (i%2 == 0) {
              document.getElementById('akapit').style.color = 'red'
       }
       else {
              document.getElementById('akapit').style.color = myPrecious;
       };
       i++;
};

function dodajKomentarz(){
       let komentarz = document.getElementById('comment').value;
       document.getElementById('kom1').innerText = komentarz;
};
