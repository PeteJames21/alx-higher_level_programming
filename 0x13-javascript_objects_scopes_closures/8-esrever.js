#!/usr/bin/node
// Reverse a list

exports.esrever = function (list) {
  const result = [];
  const listCopy = list.slice();

  while (listCopy.length) {
    result.push(listCopy.pop());
  }

  return result;
};
