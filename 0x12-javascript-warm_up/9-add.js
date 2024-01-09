#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}

const [, , first, second] = process.argv;
add(parseInt(first), parseInt(second));
