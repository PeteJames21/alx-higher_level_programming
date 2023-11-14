#!/usr/bin/node
// Find and print the second largest commandline argument.
// It is assumeed that all the arguments are integers

// Get the commandline arguments
const args = process.argv.slice(2, process.argv.length);
if (args.length < 2) {
  console.log(0);
} else {
  // Convert the array elements to integers
  const intArgs = args.map(x => parseInt(x, 10));
  // Sort the array and find the secona largest element
  console.log(intArgs.sort()[intArgs.length - 2]);
}
