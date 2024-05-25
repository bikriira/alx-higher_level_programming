#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const movie = JSON.parse(body);
    const characters = movie.characters;
    const totalCharacters = characters.length;
    let index = 0;

    /**
     * Recursively fetches and prints the names of characters
     * from the given list of character URLs in sequential order(to avoid asynchrounous)
     *
     * @param {Array} characterUrls - Array of URLs to fetch character details.
     */
    function fetchCharacter (characterUrls) {
      if (index >= totalCharacters) return;
      request(characterUrls[index], (error, response, body) => {
        if (!error && response.statusCode === 200) {
          console.log(JSON.parse(body).name);
          index++;
          fetchCharacter(characterUrls);
        }
      });
    }

    fetchCharacter(characters);
  }
});
