const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../test.txt")
  .toString()
  .trim()
  .split("\n");

function solution(N, M, students) {
  const visited = new Array(N + 1).fill(-1);
  const targets = new Array(N + 1).fill(null).map((_, idx) => idx);
  let cnt = 0;

  function findTarget(n) {
    if (targets[n] === n) return n;

    targets[n] = findTarget(targets[n]);
    return targets[n];
  }

  for (let student = 0; student < M; student++) {
    const [a, b] = students[student];
    book = findTarget(b);

    if (book >= a && book > 0 && visited[book] === -1) {
      visited[book] = student;
      targets[book] = findTarget(book - 1);
      cnt++;
    }
  }
  return cnt;
}

const T = parseInt(input[0]);
let idx = 1;

for (let t = 0; t < T; t++) {
  const [N, M] = input[idx++].split(" ").map((item) => parseInt(item));
  const students = [];
  for (let i = 0; i < M; i++) students.push(input[idx++].split(" ").map((item) => parseInt(item)));
  students.sort((a, b) => b[0] - a[0]);
  console.log(solution(N, M, students));
}
