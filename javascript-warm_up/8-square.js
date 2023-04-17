#!/usr/bin/node
const size = process.argv[2];
if (isNaN(size)) {
  console.log('Missing size');
} else {
  let side = 'X';
  let i = 1;
  while (i < size) {
    side += 'X';
    i++;
  }
  let j = 0;
  while (j < size) {
    console.log(side);
    j++;
  }
}
