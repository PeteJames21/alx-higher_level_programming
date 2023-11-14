#!/usr/bin/node
/* Add the first two args passed to the commandline.
* The args are expected to be ints.
*/

function add (a, b) {
  console.log(a + b);
}

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

add(a, b);
