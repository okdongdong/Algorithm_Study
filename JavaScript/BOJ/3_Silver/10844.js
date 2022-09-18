const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../test.txt")
  .toString()
  .trim()
  .split("\n");

const N = parseInt(input);

const arr = new Array(N - 1).fill(null).map(() => new Array(10).fill(0));

arr.unshift(new Array(10).fill(1));
arr[0][0] = 0;

for (let i = 1; i < N; i++) {
  arr[i][0] = arr[i - 1][1];
  arr[i][9] = arr[i - 1][8];
  for (let j = 1; j < 9; j++) arr[i][j] = (arr[i - 1][j + 1] + arr[i - 1][j - 1]) % 1000000000;
}

console.log(arr[N - 1].reduce((a, b) => (a + b) % 1000000000, 0));
