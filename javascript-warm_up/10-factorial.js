#!/usr/bin/node

// Print a factorial.

const arg1 = (Number(process.argv[2]));

function printFactorial (arg1) {
  // Check for 0!
  // Check if arg1 is not a number.
  if ((isNaN(arg1)) || (arg1 === 0)) {
    return 1;
  // Recursion: the function calls itself until it reaches 0.
  } else {
    return arg1 * (printFactorial(arg1 - 1));
  }
}

console.log(printFactorial(arg1));
