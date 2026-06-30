#!/usr/bin/node

// Print 3 lines with an array and a loop.

const strArray = [];
strArray.push('C is fun', 'Python is cool', 'JavaScript is amazing');

let i, x;

for (i = 0, x = 0; i <= 2; i++, x++) {
  console.log(strArray[x]);
}
