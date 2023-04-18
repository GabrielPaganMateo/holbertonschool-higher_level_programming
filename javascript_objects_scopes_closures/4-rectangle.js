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
        const tmp_h = this.height;
        const tmp_w = this.width;
        this.width = tmp_h;
        this.height = tmp_w;
    }

    double () {
      this.width += this.width;
      this.height += this.height;
    }
  }
  
  module.exports = Rectangle;
  