const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../test.txt")
  .toString()
  .trim()
  .split("\n");

const [N, K] = input.map((n) => parseInt(n));

function smallNumCnt(N, num) {
  let cnt = 0;
  for (let i = 1; i <= Math.min(num, N); i++) cnt += Math.min(N, num / i) >> 0;
  return cnt;
}

function solution(N, K) {
  let [left, right] = [1, Math.min(N ** 2, 10 ** 9) + 1];
  while (left < right) {
    let mid = ((left + right) / 2) >> 0;

    const cnt = smallNumCnt(N, mid);
    if (cnt < K) left = mid + 1;
    else right = mid;
  }

  return left;
}

console.log(solution(N, K));
