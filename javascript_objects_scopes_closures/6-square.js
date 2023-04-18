#!/usr/bin/node

const PapaSquare = require('./5-square');

class Square extends PapaSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let i = 0;
    let length = '';
    while (i < this.width) {
      length += c;
      i++;
    }
    let j = 0;
    while (j < this.height) {
      console.log(length);
      j++;
    }
  }
}

module.exports = Square;
