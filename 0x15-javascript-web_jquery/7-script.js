#!/usr/bin/node

let URL = "https://swapi-api.alx-tools.com/api/people/5/?format=json"

$(document).ready(function() {
    fetch(URL)
    .then(resp => resp.json())
    .then(data => {
        $('#character').text(data.name);
    })
    .catch(error => console.error(error));
});
