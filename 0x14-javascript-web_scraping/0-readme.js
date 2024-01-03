#!/usr/bin/node
// Read a file and print its contents to stdout. Filename is the first
// argument passed to this script.

const fs = require('fs');
const filename = process.argv[2];

if (!filename) {
  console.error('Usage: <./0-readme.js <fileName>');
  process.exit(1);
}

fs.readFile(filename, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }

  console.log(data);
});
