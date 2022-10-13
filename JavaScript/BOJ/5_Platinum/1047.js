const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../test.txt")
  .toString()
  .trim()
  .split("\n");

const [[N], ...trees] = input.map((a) => a.split(" ").map((b) => parseInt(b)));

let x_fence = new Set();
let y_fence = new Set();

for (let [x, y] of trees) {
  x_fence.add(x);
  y_fence.add(y);
}

x_fence = [...x_fence];
y_fence = [...y_fence];

x_fence.sort((a, b) => a - b);
y_fence.sort((a, b) => a - b);

const [X, Y] = [x_fence.length, y_fence.length];
let minCnt = N;

for (let x_min = 0; x_min < X; x_min++) {
  for (let x_max = x_min; x_max < X; x_max++) {
    for (let y_min = 0; y_min < Y; y_min++) {
      for (let y_max = y_min; y_max < Y; y_max++) {
        let cnt = 0;
        let targetVal = (x_fence[x_max] - x_fence[x_min] + y_fence[y_max] - y_fence[y_min]) * 2;
        const treeInArea = [];

        for (let [x, y, val] of trees) {
          if (x_fence[x_min] <= x && x <= x_fence[x_max] && y_fence[y_min] <= y && y <= y_fence[y_max]) {
            treeInArea.push(val);
          } else {
            cnt++;
            targetVal -= val;
          }
        }

        treeInArea.sort((a, b) => a - b);

        while (targetVal > 0) {
          targetVal -= treeInArea.pop();
          cnt++;
        }

        minCnt = Math.min(minCnt, cnt);
      }
    }
  }
}

console.log(minCnt);
