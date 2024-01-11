#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w < 1 || isNaN(w) || h < 1 || isNaN(h)) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const w = this.width;
    const h = this.height;
    this.height = w;
    this.width = h;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}

module.exports = Rectangle;
