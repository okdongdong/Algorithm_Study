const fs = require("fs");
// const input = fs.readFileSync("/dev/stdin").toString().trim();
const input = fs.readFileSync("../test.txt").toString().trim();

const N = parseInt(input);

let a = 5;
let result = 0;
while (a <= N) {
  result += Math.floor(N / a);
  a *= 5;
}

console.log(result);
