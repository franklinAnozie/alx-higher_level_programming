#!/usr/bin/node

const newList = require('./100-data').list;

const mapper = (list) => {
  const mapped = list.map((x, i) => x * i);
  return mapped;
};

console.log(newList);
console.log(mapper(newList));
