#!/usr/bin/node

let args = require('process').argv;

if (args.length > 3) {
  args = args.slice(2);
  args = args.map(num => parseInt(num)); // Parse strings to integers
  args.sort((a, b) => a - b); // Custom comparison function to sort numbers
  console.log(args[args.length - 2]); // Print the second largest number
} else {
  console.log('0');
}
