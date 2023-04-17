#!/usr/bin/node
const process = require('process');
const argumentValue = process.argv[2];
if (argumentValue !== undefined) {
  console.log(argumentValue);
} else {
  console.log('No argument');
}
