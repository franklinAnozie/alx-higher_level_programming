#!/usr/bin/node
const printC = () => {
  const arg = parseInt(process.argv[2]);
  const toPrint = 'C is fun';
  if (arg) {
    for (let i = 0; i < arg; i++) {
      console.log(toPrint);
    }
  } else {
    console.log('Missing number of occurrences');
  }
};

printC();
