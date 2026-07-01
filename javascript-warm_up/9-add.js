#!/usr/bin/node

// Print the addition of two integers.

const arg1 = Math.floor(Number(process.argv[2]));
const arg2 = Math.floor(Number(process.argv[3]));

function add (a, b) {
  return a + b;
}
console.log(add(arg1, arg2));
