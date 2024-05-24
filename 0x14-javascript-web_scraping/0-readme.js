#!/usr/bin/node

const fs = require('fs').promises;
const fileName = require('process').argv[2];

async function readFile (fileName) {
  try {
    const fileContent = await fs.readFile(fileName, 'utf-8');
    console.log(fileContent);
  } catch (error) {
    console.log(error);
  }
}
readFile(fileName);
