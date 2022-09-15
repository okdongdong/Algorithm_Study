const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../test.txt")
  .toString()
  .trim()
  .split("\n");

const [T, ...tcList] = input;

for (let tc of tcList) {
  const [r, e, c] = tc.split(" ").map((t) => parseInt(t));
  console.log(r < e - c ? "advertise" : r > e - c ? "do not advertise" : "does not matter");
}
