#!/usr/bin/node

const process = require('process');
const rounds = process.argv[2];

if (isNaN(rounds)) {
  console.log('Missing size');
} else {
  for (let index = 0; index < rounds; index++) {
    let row = '';
    for (let j = 0; j < rounds; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
