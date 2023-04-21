#!/usr/bin/node
const request = require('request');
const process = require('process');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const obj = {};
    const tasks = JSON.parse(body);
    let taskCount = 0;
    let userCount = 1;
    for (let i = 0; i < tasks.length; i++) {
      if (tasks[i].userId !== userCount) {
        userCount++;
        taskCount = 0;
      }
      const user = tasks[i].userId;
      if (tasks[i].completed === true) {
        taskCount++;
      }
      if (taskCount !== 0) {
        obj[user] = taskCount;
      }
    }
    console.log(obj);
  }
});
