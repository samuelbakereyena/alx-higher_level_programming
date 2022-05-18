#!/usr/bin/node
exports.logMe = function (list){
	if (!this.count) {
    this.count = 0;
  }
  console.log(`${this.count}: ${item}`);
  this.count++;
};
