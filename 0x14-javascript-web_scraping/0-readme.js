#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', (err, fileData) => {
    if (err) {
        console.error(err);
    }else{
        console.log(fileData);
    }
});
