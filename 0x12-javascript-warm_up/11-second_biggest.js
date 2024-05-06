#!/usr/bin/node

const args = require('process').argv;

let biggestNum = 0;
let secBiggestNUm = 0;
if (args.length >= 4) {
  for (let i = 2; i < args.length; i++) {
    if (args[i] >= biggestNum) {
      secBiggestNUm = biggestNum;
      biggestNum = args[i];
    }
  }
  console.log(secBiggestNUm);
} else {
  console.log('0');
}
