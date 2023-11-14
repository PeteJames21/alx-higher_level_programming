#!/usr/bin/node
// Convert the first command line argument to an integer and print it

const arg = parseInt(process.argv[2]);

if (!arg) {
  console.log('Not a number');
} else {
  console.log('My number:', arg);
}
