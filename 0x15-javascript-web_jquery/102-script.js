#!/usr/bin/node

let URL = "https://hellosalut.stefanbohacek.dev/"

$(document).ready(function() {
    $('#btn_translate').click(function() {
        const val = $('#language_code').val();
        const append = `${URL}?lang=${val}`;
        fetch(append)
        .then(resp => resp.json())
        .then(data => {
            $('#hello').text(data.hello);
        })
        .catch(error => console.error(error));
    });
});
