#!/usr/bin/env node

const request = require('request');
const URL = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(URL, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    const body = response.toJSON().body;
    console.log(JSON.parse(body).title);
  }
});
