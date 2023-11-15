#!/usr/bin/node
// Return a function that converts its argument to a given base (concept: closures).

exports.converter = function (base) {
  return (n) => n.toString(base);
};
