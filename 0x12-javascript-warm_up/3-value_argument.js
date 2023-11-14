#!/usr/bin/node
// Print the first arg passed to the script

const args = process.argv;
if (args[2]) {
  console.log(args[2]);
} else {
  console.log('No argument');
}
