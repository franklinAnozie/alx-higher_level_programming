#!/usr/bin/node

$(document).ready(function() {
    $('#update_header').click(function() {
        let newHeader = 'New Header!!!';
        $('header').text(newHeader);
    });
});
