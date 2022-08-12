const fs = require("fs");
// const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const input = fs.readFileSync("../test.txt").toString().trim().split("\n");

const N = parseInt(input[0]);
const edges = input.slice(1);
const nodes = [];

for (let i = 0; i < N + 1; i++) {
  nodes.push([]);
}

for (edge of edges) {
  const [node1, node2] = edge.split(" ").map(Number);

  nodes[node1].push(node2);
  nodes[node2].push(node1);
}

const parents = { 1: 1 };

const findChild = (parent) => {
  for (child of nodes[parent]) {
    if (!parents[child]) {
      parents[child] = parent;
      findChild(child);
    }
  }
};

findChild(1);

let result = "";

for (let node = 2; node < N + 1; node++) {
  result += parents[node] + "\n";
}

console.log(result);
