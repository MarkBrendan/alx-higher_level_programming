#!/usr/bin/node

exports.esrever = function (list) {
  let revs = [];
  for (let i = list.length -1; i >= list.length; i--) {
    revs.push(list[i]);
  }
  return revs;
};
