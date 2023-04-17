#!/usr/bin/node
let arg = process.argv[2];
let i = 0;
if (arg <= 0) {
  
} else if (arg >= 0) {
    while (i < arg) {
        console.log('C is fun');
        i++;
    }
} else {
    console.log('Missing number of occurrences');
}