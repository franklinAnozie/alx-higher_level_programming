#!/usr/bin/node

const request = require('request');
const args = process.argv;
const URL = `https://swapi-api.alx-tools.com/api/films/${args[2]}`;

const getData = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
};

const getNames = async (url) => {
  try {
    let links = await getData(url);
    links = links.characters;
    for (const link of links) {
      const characterName = await getData(link);
      console.log(characterName.name);
    }
  } catch (error) {
    console.error(error);
  }
};

getNames(URL);
