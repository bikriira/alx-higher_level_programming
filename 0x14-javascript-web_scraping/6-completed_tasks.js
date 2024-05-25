#!/usr/bin/node

const request = require('request');
const params = require('process').argv;

const completedTodos = {};

request(params[2], (error, response, body) => {
  if (!error) {
    const todos = JSON.parse(body);
    todos.forEach(currentTodo => {
      if (currentTodo.completed) {
        if (!completedTodos[currentTodo.userId]) {
          completedTodos[currentTodo.userId] = 0;
          console.log('dfgf');
        }
        completedTodos[currentTodo.userId] += 1;
      }
    });
    console.log(completedTodos);
  } else {
    console.log(error);
  }
});
