#!/usr/bin/node

const request = require('request');
const params = require('process').argv;
const fs = require('fs');

request(params[2], (error, response, body) => {
  if (!error) {
    fs.writeFile(params[3], body, 'utf-8', (err) => {
      if (err) {
        console.error(`Error writing to file: ${err}`);
      }
    });
  } else {
    console.log(error);
  }
});
