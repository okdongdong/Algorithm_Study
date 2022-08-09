const fs = require("fs");
// const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
const input = fs.readFileSync("../test.txt").toString().trim().split("\n");
const [N, K] = input[0].split(" ").map(Number);

const students = input.slice(1);
const studentsCnt = {
  1: 0,
  20: 0,
  21: 0,
  30: 0,
  31: 0,
};

for (student of students) {
  const [a, b] = student.split(" ").map(Number);

  if ((b + 1) >> 1 === 1) {
    studentsCnt[1] += 1;
  } else {
    const key = `${(b + 1) >> 1}${a}`;
    studentsCnt[key] += 1;
  }
}

let result = 0;
for (cnt in studentsCnt) {
  result += Math.ceil(studentsCnt[cnt] / K);
}

console.log(result);
