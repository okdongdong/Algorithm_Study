let fs = require("fs");
let input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../test.txt")
  .toString()
  .trim()
  .split("\n");

const [[N, M], trees] = input.map((i) => i.split(" ").map((n) => parseInt(n)));

function solution(N, M, trees) {
  let minHeight = 0;
  let maxHeight = 1000000000;
  while (minHeight < maxHeight) {
    targetHeight = ((minHeight + maxHeight) / 2) >> 0;
    const totalLength = trees.reduce((total, tree) => total + Math.max(0, tree - targetHeight), 0);

    if (totalLength >= M) minHeight = targetHeight + 1;
    else maxHeight = targetHeight - 1;
  }
  return maxHeight;
}

console.log(solution(N, M, trees));
