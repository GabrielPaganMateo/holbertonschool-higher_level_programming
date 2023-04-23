#!/usr/bin/node
const url = 'https://swapi-api.hbtn.io/api/films/?format=json'
$.getJSON(url, function(data) {
    const films = data.results
    for (const film of films)
    $("#list_movies").append('<li>' + film.title + '</li>')
})