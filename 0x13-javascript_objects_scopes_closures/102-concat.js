#!/usr/bin/node

const fs = require('fs');
const args = process.argv;

const concat = () => {
  if (args.length !== 5) {
    console.log('Error, file path not correct');
  } else {
    let fileContent = fs.readFileSync(args[2], 'utf8');
    fileContent += fs.readFileSync(args[3], 'utf8');
    fs.writeFileSync(args[4], fileContent);
  }
};

concat();
