#!/usr/bin/node

const promisify = require('util').promisify;
let request = require('request');
request = promisify(request);

const urlParam = require('process').argv[2];

(async () => {
  const response = await request(urlParam);
  const movies = JSON.parse(response.body).results;
  let counter = 0;

  movies.forEach(movie => {
    for (let i = 0; i < movie.characters.length; i++) {
      if (movie.characters[i] === 'https://swapi-api.alx-tools.com/api/people/1/') {
        counter++;
      }
    }
  });
  console.log(counter);
})();
