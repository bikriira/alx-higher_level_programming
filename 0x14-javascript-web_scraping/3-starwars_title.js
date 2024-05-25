#!/usr/bin/node

const request = require('request');
const episodeId = require('process').argv[2];
const urlParam = `https://swapi-api.alx-tools.com/api/films/${episodeId}`;

request(urlParam, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
