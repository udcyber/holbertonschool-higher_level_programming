#!/usr/bin/node

// Write My number: (number) if the 1st argument can be converted to an integer.
// Else, write "Not a number".

const firstArg = process.argv[3];

if (Number.isInteger(firstArg)) {
  console.log('My number: ');
}

console.log('My number: <first argument converted in integer>');
