#!/usr/bin/node

// Print a message depending on the number of arguments passed.

const argNumber = process.argv.length;

if (argNumber === 2) {
  console.log('No argument');
} else if (argNumber === 3) {
  console.log('Argument found');
} else if (argNumber > 3) {
  console.log('Arguments found');
}
