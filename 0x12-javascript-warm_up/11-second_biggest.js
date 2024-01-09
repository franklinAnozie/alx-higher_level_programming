#!/usr/bin/node
const secondBiggest = () => {
  const args = process.argv;
  let minimun = 0;
  if (args.length < 4) {
    return minimun;
  } else {
    minimun = parseInt(args[2]);
    for (let i = 3; i < args.length; i++) {
      if (args[i] < minimun) {
        minimun = parseInt(args[i]);
      }
    }
    return minimun;
  }
};

console.log(secondBiggest());
