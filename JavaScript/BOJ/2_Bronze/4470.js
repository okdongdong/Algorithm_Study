const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../test.txt")
  .toString()
  .trim()
  .split("\n");

const [n, ...txt] = input;

txt.forEach((t, idx) => console.log(`${idx + 1}. ${t}`));
