#!/usr/bin/node

const fs = require('fs').promises;
const fileName = require('process').argv[2];
const fileContent = require('process').argv[3];

async function writeToFile (fileContent) {
  try {
    await fs.writeFile(fileName, fileContent, 'utf-8');
  } catch (error) {
    console.log(error);
  }
}
writeToFile(fileContent);
