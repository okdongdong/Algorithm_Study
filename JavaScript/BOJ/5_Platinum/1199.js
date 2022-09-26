let fs = require("fs");
let input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../test.txt")
  .toString()
  .trim()
  .split("\n");

let [N, ...arr] = input;
N = parseInt(N);
input = null;

let edges = new Array(N).fill(null).map(() => new Object());

function dfs(i) {
  for (let j in edges[i]) {
    if (edges[i][j] > 0) {
      edges[i][j]--;
      edges[j][i]--;
      dfs(j);
    }
  }
  process.stdout.write(`${parseInt(i) + 1} `);
}

function solution() {
  for (let i = 0; i < N; i++) {
    let nodes = arr[i].split(" ").map((n) => parseInt(n));
    for (let j = i + 1; j < N; j++) {
      if (nodes[j]) {
        edges[i][j] = nodes[j];
        edges[j][i] = nodes[j];
      }
    }
    if (nodes.reduce((a, b) => a + b, 0) % 2) return console.log(-1);
  }
  arr = null;
  dfs(0);
}

solution();
