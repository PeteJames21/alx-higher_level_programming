#!/usr/bin/node
// Compute and print the number of tasks completed by user id.

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  try {
    const todos = JSON.parse(body);
    const completed = {};

    todos.forEach((todo) => {
      if (todo.completed) {
        completed[todo.userId] = (completed[todo.userId] || 0) + 1;
      }
    });

    console.log(completed);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});

