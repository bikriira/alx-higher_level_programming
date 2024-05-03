#!/usr/bin/node

const process = require('process');
const myArg = process.argv[2];

if (isNaN(myArg)) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(myArg));
}
