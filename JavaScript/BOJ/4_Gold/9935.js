const fs = require("fs");
// const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
const input = fs.readFileSync("../test.txt").toString().trim().split("\n");

const txt = input[0].trim();
const bomb = input[1];
const result = [];

for (let i = 0; i < txt.length; i++) {
  result.push(txt[i]);
  if (result.length >= bomb.length) {
    const idx = result.length - bomb.length;
    if (result.slice(idx).join("") === bomb) result.splice(idx, bomb.length);
  }
}

console.log(result.length === 0 ? "FRULA" : result.join(""));
