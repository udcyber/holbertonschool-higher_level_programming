#!/usr/bin/node

// Search the second biggest integer in the list of arguments.
// Assume all arguments can be converted to integer.

// Check if the list is empty or only has one argument.
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const argList = process.argv.map(Number)
    .slice(2, process.argv.length)
    .sort((a, b) => a - b);
  console.log(argList[argList.length - 2]);
}
