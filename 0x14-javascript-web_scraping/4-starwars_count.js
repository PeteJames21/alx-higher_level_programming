#!/usr/bin/node
// Print the number of movies where the character "Wedge Antilles" is present.

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  try {
    const movies = JSON.parse(body).results;
    const count = movies.reduce((acc, movie) => {
      return movie.characters.some((character) => character.endsWith('/18/'))
        ? acc + 1
        : acc;
    }, 0);

    console.log(count);
  } catch (parseError) {
    console.error(parseError);
  }
});
