#!/usr/bin/node

let URL = "https://hellosalut.stefanbohacek.dev/?lang=fr"

$(document).ready(function() {
    fetch(URL)
    .then(resp => resp.json())
    .then(data => {
        $('#hello').text(data.hello);
    })
    .catch(error => console.error(error));
});
