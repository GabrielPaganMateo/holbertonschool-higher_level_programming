#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      // empty object
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    let length = '';
    while (i < this.width) {
      length += 'X';
      i++;
    }
    let j = 0;
    while (j < this.height) {
      console.log(length);
      j++;
    }
  }

  rotate () {
    const tmpH = this.height;
    const tmpW = this.width;
    this.width = tmpH;
    this.height = tmpW;
  }

  double () {
    this.width += this.width;
    this.height += this.height;
  }
}

module.exports = Rectangle;
