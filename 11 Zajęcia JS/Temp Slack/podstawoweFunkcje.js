//alert('Działa!');

let data = new Date();
//alert(data.getFullYear());
let obj = {0:"Styczeń",
       1:"Luty",
       2:"Marzec",
       3:"Kwiecień"};
//alert(obj[data.getMonth()] +' '+data.getFullYear());

console.log("Hello world");
console.log(obj);

function PokazDate(prefix){
  alert(prefix+' '+obj[data.getMonth()] +' '+data.getFullYear());
};


function zmienKolor(){
  document.getElementById('akapit').style.color = 'red';
};


function dodajKomentarz() {
  let komentarz = document.getElementById('comment').value;
  document.getElementById('kom1').innerText = komentarz;
}
