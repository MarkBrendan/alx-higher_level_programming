#!/usr/bin/node

const args = process.argv;
if (args[2] === undefined) {
  console.log('undefined ' + 'is ' + 'undefined');
} else if (!args[3] || !args[4]) {
  console.log(args[2] + ' is ' + args[3]);
} else if (!args[3] || args[4] === undefined) {
  console.log(args[2] + ' is ' + 'undefined');
}
