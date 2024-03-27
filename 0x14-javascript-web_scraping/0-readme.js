#!/usr/bin/node

const readme = require('fs');
const args = process.argv[2];

readme.readFile(args, 'utf-8', (error, response) => {
  if (error) {
    console.log(error);
  } else {
    console.log(response);
  }
});
