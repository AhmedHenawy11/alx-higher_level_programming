#!/usr/bin/node

class Rectangle {
    constructor(w, h) {
        this.width = w;
        this.height = h;
    }
}
module.exports = Rectangle;

const r = new Rectangle(5, 7);

console.log(r);