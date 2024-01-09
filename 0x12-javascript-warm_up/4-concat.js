#!/usr/bin/node
const printArgs = () => {
  const args = process.argv;
  console.log(`${args[2]} is ${args[3]}`);
};

printArgs();
