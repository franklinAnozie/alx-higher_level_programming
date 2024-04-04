#!/usr/bin/node

$(document).ready(function() {
    $('#add_item').click(function() {
        let newElement = $("<li>Item</li>");
        $('.my_list').append(newElement);
    });
});
