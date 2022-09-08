const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../test.txt")
  .toString()
  .trim()
  .split("\n");

const [K, ...nums] = input.map((n) => parseInt(n));
const stack = [];

for (let num of nums) {
  if (num === 0) stack.pop();
  else stack.push(num);
}

console.log(stack.reduce((prev, curr) => prev + curr, 0));
