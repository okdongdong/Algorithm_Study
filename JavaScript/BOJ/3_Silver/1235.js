const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../test.txt")
  .toString()
  .trim()
  .split("\n");

const N = parseInt(input[0]);
const [, ...students] = input.map((a) => a.trim());

const L = students[0].length;

function solution(L, students) {
  for (let i = L - 1; i >= 0; i--) {
    const temp = new Set();
    let flag = true;
    for (let student of students) {
      let endNum = student.slice(i, L);

      if (temp.has(endNum)) {
        flag = false;
        break;
      }
      temp.add(endNum);
    }
    if (flag) return L - i;
  }
}

console.log(solution(L, students));
