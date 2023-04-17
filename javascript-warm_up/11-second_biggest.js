#!/usr/bin/node
const args = process.argv;

if (args[2] === undefined) {
  console.log('0');
} else if (args.length === 3) {
  console.log('0');
} else {
  let big = Number.MIN_SAFE_INTEGER;
  let small = Number.MIN_SAFE_INTEGER;
  let i = 2;
  while (i <= args.length) {
    if (parseInt(args[i]) > big) {
      small = big;
      big = parseInt(args[i]);
    } else if (parseInt(args[i]) > small && parseInt(args[i]) !== big) {
      small = parseInt(args[i]);
    }
    i++;
  }
  console.log(small);
}
