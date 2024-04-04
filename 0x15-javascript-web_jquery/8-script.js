#!/usr/bin/node

let URL = "https://swapi-api.alx-tools.com/api/films/?format=json"

$(document).ready(function() {
    fetch(URL)
    .then(resp => resp.json())
    .then(data => {
        const new_data = data.results;
        new_data.forEach((list) => {
            $('#list_movies').append(`<li>${list.title}</li>`);
        })
    })
    .catch(error => console.error(error));
});
