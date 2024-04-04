#!/usr/bin/node
// This script updates the text color
// of the header element to red

const colorChange = () => {
    let head = document.querySelector('header');
    head.style.color = '#FF0000';
};

colorChange();
