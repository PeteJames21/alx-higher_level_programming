#!/usr/bin/node
// Write a string to a file. The filaname is the first argument to this script
// The string to write is the second arg.
const fs = require('fs');

const filePath = process.argv[2];
const contentToWrite = process.argv[3];

if (!filePath || !contentToWrite) {
  console.error('Usage: ./1-writeme.js FILENAME STRING');
  process.exit(1);
}

fs.writeFile(filePath, contentToWrite, 'utf8', error => {
  if (err) {
    console.error(error);
  }
});
