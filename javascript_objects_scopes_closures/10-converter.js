#!/usr/bin/node

exports.converter = function (base) {
  const conversion = function (num) {
    return num.toString(base);
  };
  return conversion;
};
