#!/usr/bin/node
const { argv } = require('process');
const argc = argv.length;

function add (a, b) {
    return parseInt(a) + parseInt(b); 
}


console.log(argc === 3 ? add(argv[2], argv[3]) : "NaN" );
