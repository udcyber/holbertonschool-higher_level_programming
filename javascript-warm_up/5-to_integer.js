#!/usr/bin/node

// Write "My number: (number)"" if the 1st argument can be converted to an integer.
// Else, write "Not a number".

// Math.floor to change the number into an integer (fi 89.89 becomes 89).
const firstArg = Math.floor(Number(process.argv[2]));

if (Number.isInteger(firstArg) === true) {
  console.log(`My number: ${firstArg}`);
} else {
  console.log('Not a number');
}
