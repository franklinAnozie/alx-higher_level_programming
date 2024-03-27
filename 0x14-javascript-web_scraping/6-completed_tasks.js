#!/usr/bin/node

const request = require('request');
const args = process.argv;
const listOfComp = {};

request(args[2], (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const bodyResp = JSON.parse(body);
    bodyResp.forEach(element => {
      if (element.completed) {
        const uid = element.userId;
        if (listOfComp[uid]) {
          listOfComp[uid] = listOfComp[uid] + 1;
        } else {
          listOfComp[uid] = 1;
        }
      }
    });
    console.log(listOfComp);
  }
});
