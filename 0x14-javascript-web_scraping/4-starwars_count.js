#!/usr/bin/node

const request = require('request');
const args = process.argv;

request(args[2], (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const result = JSON.parse(body).results;
    const arrOc = [];
    let count = 0;
    result.forEach((value) => {
      arrOc.push(value.characters);
    });
    arrOc.map((characters) => {
      return characters.filter((character) => {
        return character.includes('/18/') ? count++ : null;
      });
    });
    console.log(count);
  }
});
