#!/usr/bin/node
const secondBiggest = () => {
  const args = process.argv;
  let newArgs = [];
  let j = 0;
  let second = 0;
  if (args.length < 4) {
    return second;
  } else {
    for (let i = 2; i < args.length; i++) {
      newArgs[j] = parseInt(args[i]);
      j++;
    }
    newArgs = newArgs.sort((a, b) => a - b);
    second = newArgs.reverse()[1];
    return second;
  }
};

console.log(secondBiggest());
