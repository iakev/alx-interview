#!/usr/bin/node
// Retrieves characters of specified movie and list them
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

const getCharsUrl = function (options) {
  return new Promise((resolve, reject) => {
    request.get(options, (error, response, body) => {
      if (response.statusCode === 200) {
        const data = JSON.parse(body);
        const characters = data.characters;
        resolve(characters);
      } else if (error) {
        reject(error);
      }
    });
  });
};

async function getCharacterName (characterUrl) {
  return new Promise((resolve, reject) => {
    request.get(characterUrl, (error, response, body) => {
      if (response.statusCode === 200) {
        const character = JSON.parse(body);
        const characterName = character.name;
        resolve(characterName);
      } else if (error) {
        reject(error);
      }
    });
  });
}

async function getCharactersName (options) {
  const characters = await getCharsUrl(options);
  for (let index = 0; index < characters.length; index++) {
    const characterUrl = characters[index];
    const characterName = await getCharacterName(characterUrl);
    console.log(characterName);
  }
}

getCharactersName(url);
