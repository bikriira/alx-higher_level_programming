#!/usr/bin/node

const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (!error) {
    const results = JSON.parse(body).results;
    const occurrence = results.reduce((count, movie) => {
      return count + (movie.characters.find((character) => character.endsWith('/18/')) ? 1 : 0);
    }, 0);

    console.log(occurrence);
  }
});
