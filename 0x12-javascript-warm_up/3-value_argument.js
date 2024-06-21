#!/usr/bin/node

const { argv } = require('process');
const argc = argv.length;

argv.forEach(() => len++);

console.log(len === 2 ? 'No argument' : argv[2]);
