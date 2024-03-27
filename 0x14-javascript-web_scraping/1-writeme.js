#!/usr/bin/env node

const fs = require('fs');
const args = process.argv;

const fp = args[2];
const str2r = args[3];

fs.writeFile(fp, str2r, 'utf-8', (error) => {
  if (error) {
    console.error(error);
  }
});
