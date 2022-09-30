const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../test.txt")
  .toString()
  .trim()
  .split("\n");

const [G, P, ...gates] = input.map((n) => parseInt(n));

const dockableGates = new Array(G + 1).fill(null).map((_, idx) => idx);

function findGate(gate) {
  if (dockableGates[gate] === gate) return gate;
  dockableGates[gate] = findGate(dockableGates[gate]);
  return dockableGates[gate];
}

let cnt = 0;
for (let p = 0; p < P; p++) {
  const gate = findGate(gates[p]);
  if (gate === 0) break;
  dockableGates[gate] = dockableGates[gate - 1];
  cnt++;
}
console.log(cnt);
