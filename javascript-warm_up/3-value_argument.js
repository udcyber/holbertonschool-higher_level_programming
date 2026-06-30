#!/usr/bin/node

// Print the first argument passed.
// Return "No argument" if no arguments are passed.

const argNum1 = process.argv[2];

if (typeof argNum1 === 'undefined') {
  console.log('No argument');
} else {
  console.log(argNum1);
}
