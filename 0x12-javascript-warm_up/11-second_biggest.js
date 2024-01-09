#!/usr/bin/node
const secondBiggest = () => {
  let args = process.argv;
  let second = 0;
  if (args.length < 4) {
    return second;
  } else {
    args = args.sort().reverse();
    second = args[2];
    return second;
  }
};

console.log(secondBiggest());
