#!/usr/bin/node

// Update given script to replace the value 12 with 89.

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
// UPDATED CODE HERE
myObject.update({value: 12})
// UPDATED CODE HERE
console.log(myObject);
