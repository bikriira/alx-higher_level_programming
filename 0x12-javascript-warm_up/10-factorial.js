#!/usr/bin/node

const num = require('process').argv[2];

function fact (num) {
  if (num === 1 || num === undefined || num === '0') {
    return 1;
  } else {
    return num * fact(num - 1);
  }
}
console.log(fact(num));
