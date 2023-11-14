#!/usr/bin/node
/* Add the first two args passed to the commandline.
* The args are expected to be ints.
*/

function add (a, b) {
  console.log(a + b);
}

exports.add = add;
