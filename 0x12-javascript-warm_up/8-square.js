#!/usr/bin/node

const process = require('process');
const rounds = process.argv[2];

if (rounds !== undefined) {
  for (let index = 0; index < rounds; index++) {
    let row = '';
    for (let j = 0; j < rounds; j++) {
      row += 'x';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
