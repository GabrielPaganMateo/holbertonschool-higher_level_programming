#!/usr/bin/node
const arg = parseInt(process.argv[2]);

function factorial (num) {
  if (isNaN(num)) {
    return 1;
  } else if (num >= 1) {
    return num * factorial(num - 1);
  } else {
    return 1;
  }
}

const result = factorial(arg);
console.log(result);
