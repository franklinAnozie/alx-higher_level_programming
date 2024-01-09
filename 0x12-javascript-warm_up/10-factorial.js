#!/usr/bin/node
function factorial(n){
  if (n === 1 || isNaN(n)) {
    return 1;
  }
  return (n * factorial(n - 1));
};

const arg = parseInt(process.argv[2]);
console.log(factorial(arg));
