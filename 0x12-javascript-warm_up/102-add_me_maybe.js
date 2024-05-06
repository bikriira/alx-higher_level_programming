#!/usr/bin/node

function addMeMaybe (x, theFunction) {
  x++;
  theFunction(x);
}

exports.addMeMaybe = addMeMaybe;
