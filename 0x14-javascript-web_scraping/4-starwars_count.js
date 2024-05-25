#!/usr/bin/node

const promisify = require('util').promisify;
let request = require('request');
request = promisify(request);

const urlParam = require('process').argv[2];

(async () => {
  const response = await request(urlParam);
  const movies = JSON.parse(response.body).results;

  const occurrence = movies.reduce((count, movie) => {
    return count + (movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/') ? 1 : 0);
  }, 0);
  console.log(occurrence);
})();
