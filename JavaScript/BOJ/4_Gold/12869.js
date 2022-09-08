const { log } = require("console");
const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../test.txt")
  .toString()
  .trim()
  .split("\n");

const N = parseInt(input[0]);
const SCVs = [0, 0, 0];
input[1].split(" ").forEach((scv, idx) => (SCVs[idx] = scv));

const damages = [
  [1, 3, 9],
  [1, 9, 3],
  [3, 1, 9],
  [3, 9, 1],
  [9, 1, 3],
  [9, 3, 1],
];

const dp = new Array(61).fill(null).map(() => new Array(61).fill(null).map(() => new Array(61).fill(0)));

function dfs(x, y, z) {
  if (x + y + z === 0) return 0;
  if (dp[x][y][z]) return dp[x][y][z];

  let minCnt = 20;

  for (let [d1, d2, d3] of damages) {
    minCnt = Math.min(minCnt, dfs(Math.max(0, x - d1), Math.max(0, y - d2), Math.max(0, z - d3)));
  }

  dp[x][y][z] += minCnt + 1;

  return dp[x][y][z];
}

console.log(dfs(...SCVs));
