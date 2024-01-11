#!/usr/bin/node
exports.logMe = function (item) {
  if (this.numberOfargs === undefined) {
    this.numberOfargs = 0;
  } else {
    this.numberOfargs++;
  }
  console.log(`${this.numberOfargs}: ${item}`);
};
