const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../test.txt")
  .toString()
  .trim()
  .split("\n");

const [[N], nums] = input.map((a) => a.split(" ").map((b) => parseInt(b)));
const MAX_CNT = 100 * 1000 + 1;
const dp = new Array(N).fill(MAX_CNT);
dp[0] = 0;

for (let i = 0; i < N; i++) {
  const M = i + nums[i];

  for (let j = i + 1; j < Math.min(N, M + 1); j++) {
    dp[j] = Math.min(dp[j], dp[i] + 1);
  }
}

console.log(dp[N - 1] < MAX_CNT ? dp[N - 1] : -1);
