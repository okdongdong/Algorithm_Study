const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../test.txt")
  .toString()
  .trim()
  .split("\n");
const r = 31;
const M = 1234567891;
const [_, txt] = input;
const pow = new Array(51);
pow[0] = 1;
for (let i = 1; i < 51; i++) {
  pow[i] = (pow[i - 1] * r) % M;
}
const ord = (a) => a.charCodeAt() - 96;
console.log(txt.split("").reduce((p, a, i) => (p + ord(a) * pow[i]) % M, 0));
