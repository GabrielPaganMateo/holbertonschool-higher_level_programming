#!/usr/bin/node
const process = require('process');
const argumentNum = process.argv.length;
if (argumentNum === 2) {
  console.log('No argument');
} else if (argumentNum === 3) {
  console.log('Argument found');
} else if (argumentNum >= 4) {
  console.log('Arguments found');
}
