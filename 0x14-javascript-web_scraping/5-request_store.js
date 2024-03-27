#!/usr/bin/node

const request = require('request');
const fp = require('fs');
const args = process.argv;

request(args[2], 'utf-8', (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fp.writeFile(args[3], body, 'utf-8', (error) => {
      if (error) {
        console.error(error);
      }
    });
  }
});
