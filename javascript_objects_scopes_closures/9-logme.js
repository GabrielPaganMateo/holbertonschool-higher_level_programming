#!/usr/bin/node
let num = 0;
exports.logMe = function (item) {
    let str = String(num) + ':'
    console.log(str, item)
    num += 1;
}