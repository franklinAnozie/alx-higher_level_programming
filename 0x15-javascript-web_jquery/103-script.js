#!/usr/bin/node

let URL = "https://hellosalut.stefanbohacek.dev/"

$(document).ready(function() {
    const do_this = () => {
        const val = $('#language_code').val();
        const append = `${URL}?lang=${val}`;
        fetch(append)
        .then(resp => resp.json())
        .then(data => {
            $('#hello').text(data.hello);
        })
        .catch(error => console.error(error));
    };
    $('#btn_translate').click(do_this);
    $('#language_code').keypress(function(event) {
        if (event.which === 13) {
            do_this();
        };
    });
});
