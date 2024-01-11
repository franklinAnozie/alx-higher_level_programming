#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w < 1 || isNaN(w) || h < 1 || isNaN(h)) {
      return;
    }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
