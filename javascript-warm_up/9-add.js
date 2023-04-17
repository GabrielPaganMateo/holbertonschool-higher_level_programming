#!/usr/bin/node
const args = process.argv;

if (args[2] === undefined || args[3] === undefined) {
  console.log(NaN);
} else {
  const sum = parseInt(args[2]) + parseInt(args[3]);
  console.log(sum);
}
