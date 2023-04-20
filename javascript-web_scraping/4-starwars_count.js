#!/usr/bin/node
const request = require('request');
const process = require('process');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const obj = JSON.parse(body);
    const films = obj.results;
    let cameoCount = 0;
    for (let i = 0; i < films.length; i++) {
      if (films[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        cameoCount += 1;
      }
    }
    console.log(cameoCount);
  }
});
