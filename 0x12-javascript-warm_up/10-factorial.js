#!/usr/bin/node
// Compute and print the factorial of the first commandline argument

function factorial (n) {
  if (n < 0) {
    return NaN;
  }
  if (isNaN(n) || n === 0 || n === 1) {
    return 1;
  }

  return n * factorial(n - 1);
}

const arg = parseInt(process.argv[2]);
console.log(factorial(arg));
