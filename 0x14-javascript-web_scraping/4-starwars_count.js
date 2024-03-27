#!/usr/bin/env node

const request = require('request');
const URL = 'https://swapi-api.alx-tools.com/api/films/';

request(URL, (error, response, body) => {
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
      characters.filter((character) => {
        character.includes('/18/') ? count++ : null;
      });
    });
    console.log(count);
  }
});
