#!/usr/bin/node

const request = require('request');
const args = process.argv;
const URL = `https://swapi-api.alx-tools.com/api/films/${args[2]}`;

request(URL, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const result = JSON.parse(body).characters;
    result.map((link) => {
      return request(link, (error, response, body) => {
        if (error) {
          console.error(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
