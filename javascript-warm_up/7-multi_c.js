#!/usr/bin/node

// Print x times "C is fun".

let i;
const x = Math.floor(Number(process.argv[2]));

if (Number.isInteger(x) === false) {
  console.log('Missing number of occurences');
}
else {
  for (i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
