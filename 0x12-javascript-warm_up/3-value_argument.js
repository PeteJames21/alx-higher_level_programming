#!/usr/bin/node
// Print the first arg passed to the script

const args = process.argv;
if (args.length === 2) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
