let i = 0;

document.body.style.backgroundColor = 'hsl(214, 100%, 50%)';

function dodaj() {
  i--;
  console.log(i);
  document.getElementById('text').innerText = i;
  document.body.style.backgroundColor = 'hsl(214, 100%, ' + (50 + i * 5) + '%)';
};

function odejmij() {
  i++;
  document.getElementById('text').innerText = i;
  console.log(document.body.backgroundColor);
  document.body.style.backgroundColor = 'hsl(214, 100%, ' + (50 + i * 5) + '%)';
};
