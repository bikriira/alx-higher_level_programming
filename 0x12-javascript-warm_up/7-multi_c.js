#!/usr/bin/node

const process = require('process');
const rounds = process.argv[2];

if (rounds !== undefined) {
  for (let index = 0; index < rounds; index++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
