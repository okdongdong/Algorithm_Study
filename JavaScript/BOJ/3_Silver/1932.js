let fs = require("fs");
let input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../test.txt")
  .toString()
  .trim()
  .split("\n");

const [[N], ...triangle] = input.map((item) => item.split(" ").map((n) => parseInt(n)));

function solution(N, triangle) {
  const dp = new Array(N).fill(null).map((_, idx) => new Array(idx + 1).fill(0));
  dp[0][0] = triangle[0][0];

  for (let i = 0; i < N - 1; i++) {
    for (let j = 0; j < triangle[i].length; j++) {
      dp[i + 1][j] = Math.max(dp[i][j] + triangle[i + 1][j], dp[i + 1][j]);
      dp[i + 1][j + 1] = Math.max(dp[i][j] + triangle[i + 1][j + 1], dp[i + 1][j + 1]);
    }
  }

  return Math.max(...dp[N - 1]);
}

console.log(solution(N, triangle));
