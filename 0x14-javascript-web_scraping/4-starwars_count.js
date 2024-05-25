#!/usr/bin/node

const promisify = require('util').promisify;
const request = promisify(require('request'));

(async () => {
  try {
    const response = await request(process.argv[2]);
    const movies = JSON.parse(response.body).results;

    const occurrence = movies.reduce((count, movie) => {
      return count + (movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/') ? 1 : 0);
    }, 0);

    console.log(occurrence);
  } catch (error) {
    console.error('Error:', error.message);
  }
})();