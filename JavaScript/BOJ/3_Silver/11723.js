// 메모리 초과로 풀리지 않음

let fs = require("fs");
let input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../test.txt")
  .toString()
  .trim()
  .split("\n")
  .map((n) => n.trim().split(" "));

let S = new Set();
const ALL = new Array(20).fill().map((_, i) => `${i + 1}`);

let result = ``;
for (let cmd of input) {
  switch (cmd[0]) {
    case `add`:
      S.add(cmd[1]);
      break;

    case `remove`:
      S.delete(cmd[1]);
      break;

    case `check`:
      result += `${S.has(cmd[1]) ? 1 : 0}\n`;
      break;

    case `toggle`:
      if (S.has(cmd[1])) S.delete(cmd[1]);
      else S.add(cmd[1]);
      break;

    case `all`:
      S = new Set(ALL);
      break;

    case `empty`:
      S.clear();
      break;
  }
}
console.log(result);
