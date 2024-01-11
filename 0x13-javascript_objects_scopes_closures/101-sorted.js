#!/usr/bin/node

const oldDict = require('./101-data').dict;

const sortedDict = (dict) => {
  const newDict = {};
  for (const key in dict) {
    if (newDict[dict[key]] === undefined) {
      newDict[dict[key]] = [key];
    } else {
      newDict[dict[key]].push(key);
    }
  }

  return newDict;
};

console.log(sortedDict(oldDict));
