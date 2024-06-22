#!/usr/bin/node

exports.esrever = function (list) {
  const revs = [];
  for (let i = list.length - 1; i >= 0; i--) {
    revs.push(list[i]);
  }
  return revs;
};
