#!/usr/bin/node
const printInt = () => {
  const args = process.argv;
  const num = parseInt(args[2]);
  if (num) {
    console.log(`My number: ${num}`);
  } else {
    console.log('Not a number');
  }
};

printInt();
