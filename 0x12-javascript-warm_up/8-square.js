#!/usr/bin/node
const printSquare = () => {
  const arg = parseInt(process.argv[2]);
  const toPrint = 'X';
  if (arg) {
    for (let i = 0; i < arg; i++) {
      console.log(toPrint.repeat(arg));
    }
  } else {
    console.log('Missing size');
  }
};

printSquare();
