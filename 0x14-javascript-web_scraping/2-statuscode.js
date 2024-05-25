#!/usr/bin/node

const request = require('request');
const urlParam = require('process').argv[2];

request(urlParam, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
