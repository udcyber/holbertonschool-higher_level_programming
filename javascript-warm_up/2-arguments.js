#!/usr/bin/node

// Print a message depending of the number of arguments passed.

if (arguments.length === 0) {
    console.log('No argument');
}
else if (arguments.length === 1) {
    console.log('Argument found');
}
else if (arguments.length > 1) {
    console.log('Arguments found');
}
