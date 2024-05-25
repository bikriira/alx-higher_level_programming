#!/usr/bin/node

const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (!error) {
    const movies = JSON.parse(response.body).results;
    const occurrence = movies.reduce((count, movie) => {
      return count + (movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/') ? 1 : 0);
    }, 0);

    console.log(occurrence);
  }
});
