#!/usr/bin/node

const changeColor = () => {
    let header = document.querySelector('header');
    header.style.color = '#FF0000'
}

document.addEventListener('DOMContentLoaded', changeColor)
