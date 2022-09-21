const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../test.txt")
  .toString()
  .trim()
  .split("\n");

const [N, M, V] = input[0].split(" ").map((n) => parseInt(n));
const [, ...edgeInput] = input;

const edges = new Array(N + 1).fill(null).map(() => new Set());

for (let edge of edgeInput) {
  const [a, b] = edge
    .trim()
    .split(" ")
    .map((n) => parseInt(n));
  edges[a].add(b);
  edges[b].add(a);
}
edges.forEach((edge) => (edges[idx] = [...edge].sort((a, b) => a - b)));

const result = [];
const visited = new Array(N + 1).fill(false);

function dfs(currNode) {
  visited[currNode] = true;
  result.push(currNode);
  for (let nextNode of edges[currNode]) {
    if (visited[nextNode]) continue;
    dfs(nextNode);
  }

  return result;
}

function bfs(startNode) {
  let que = [startNode];
  const visited = new Array(N + 1).fill(false);
  visited[startNode] = true;
  const result = [];
  while (que.length > 0) {
    const tempQue = [];
    for (let currNode of que) {
      result.push(currNode);

      for (let nextNode of edges[currNode]) {
        if (visited[nextNode]) continue;
        visited[nextNode] = true;
        tempQue.push(nextNode);
      }
    }
    que = [...tempQue];
  }
  return result;
}

console.log(dfs(V).join(" "));
console.log(bfs(V).join(" "));
