var lata = [12, 16, 25, 14, 18, 30];

for (i=0; i<lata.length; i++){
  if (lata[i] < 13){
    console.log('dziecko');
  }
  else if (lata[i] < 18){
    console.log('nastolatek');
  }
  else if (lata[i] < 25){
    console.log('student');
  }
  else {
    console.log('dorosły');
  };
};
