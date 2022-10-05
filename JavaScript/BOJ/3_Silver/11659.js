const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../test.txt")
  .toString()
  .trim()
  .split("\n");

const [[N, M], nums, ...cmds] = input.map((a) => a.split(" ").map((b) => parseInt(b)));

const cumNums = new Array(nums.length).fill(0);
let temp = 0;
nums.forEach((num, idx) => {
  temp += num;
  cumNums[idx] = temp;
});

let result = "";
cmds.forEach((cmd) => {
  const [a, b] = cmd;
  result += `${cumNums[b - 1] - (a > 1 ? cumNums[a - 2] : 0)}\n`;
});

console.log(result);
