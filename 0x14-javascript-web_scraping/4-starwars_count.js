#!/usr/bin/node

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
    count = count + arrOc.map((characters) => {
      return characters.filter((character) => {
        return character.includes('/18/');
      });
    });
    console.log(count);
  }
});
