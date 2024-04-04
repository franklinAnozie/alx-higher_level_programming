#!/usr/bin/node

$(document).ready(function() {
    $('#add_item').click(function() {
        let newElement = $("<li>Item</li>");
        $('.my_list').append(newElement);
    })
    $('#remove_item').click(function() {
        $('.my_list > :last-child').remove();
    })
    $('#clear_list').click(function() {
        $('.my_list').empty();
    })
})
