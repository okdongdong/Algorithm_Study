const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../test.txt")
  .toString()
  .trim();

const [N, L, W, H] = input.split(" ").map((n) => parseInt(n));

let left = 0;
let right = Math.min(L, W, H);

let prevCnt = 0;

while (prevCnt < 100) {
  prevCnt++;
  let mid = (left + right) / 2;

  const lCnt = (L / mid) >> 0;
  const wCnt = (W / mid) >> 0;
  const hCnt = (H / mid) >> 0;

  let cnt = lCnt * wCnt * hCnt;

  if (cnt < N) right = mid;
  else left = mid;
}

console.log(left);
