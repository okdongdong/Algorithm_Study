const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../test.txt")
  .toString()
  .trim()
  .split("\n");

const N = parseInt(input[0]);
const nums = input[1].split(" ").map((item) => parseInt(item));
dp = new Array(N).fill(0);
dp[0] = nums[0];

for (let i = 1; i < N; i++) dp[i] = Math.max(0, dp[i - 1]) + nums[i];

console.log(Math.max(...dp));
