const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../test.txt")
  .toString()
  .trim()
  .split("\n");

const [[N, M], ...transforms] = input.map((a) => a.split(" ").map((b) => parseInt(b)));

const heads = new Array(N + 1).fill(null).map((_, idx) => idx);
const A = new Array(N + 1);
const B = new Array(N + 1);

for (let i = 1; i <= M; i++) {
  const [a, b] = transforms[i - 1];
  A[i] = a;
  B[i] = b;
}
for (let i = M; i >= 1; i--) {
  heads[A[i]] = heads[B[i]];
}

heads.shift();

console.log(...heads);
