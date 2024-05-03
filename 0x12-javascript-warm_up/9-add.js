#!/usr/bin/node

const process = require('process');
const num1 = process.argv[2];
const num2 = process.argv[3];

function add (a, b) {
  return parseInt(a) + parseInt(b);
}

console.log(add(num1, num2));
