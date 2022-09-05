const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../test.txt")
  .toString()
  .trim()
  .split("\n");

const [N, M] = input[0].split(" ").map((n) => parseInt(n));
const [, ...castle] = input;

let [temp1, temp2] = [0, 0];
for (let r = 0; r < N; r++) {
  for (let c = 0; c < M; c++) {
    if (castle[r][c] === "X") {
      temp1++;
      break;
    }
  }
}
for (let c = 0; c < M; c++) {
  for (let r = 0; r < N; r++) {
    if (castle[r][c] === "X") {
      temp2++;
      break;
    }
  }
}

console.log(Math.max(N - temp1, M - temp2));
