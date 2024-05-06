#!/usr/bin/node

let args = require('process').argv;

if (args.length > 3) {
  args = args.slice(2);
  console.log(args);
  args.sort();
  console.log(args);
  console.log(args[args.length - 2]);
} else {
  console.log('0');
}
