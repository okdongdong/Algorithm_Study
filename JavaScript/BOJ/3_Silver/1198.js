const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../test.txt")
  .toString()
  .trim()
  .split("\n");

class Point {
  constructor(point) {
    const [x, y] = point.split(" ").map((n) => parseInt(n));
    this.x = x;
    this.y = y;
  }
}

function calArea(A, B, C) {
  const area = 0.5 * Math.abs(A.x * B.y + B.x * C.y + C.x * A.y - (A.x * C.y + C.x * B.y + B.x * A.y));
  return area;
}

let [N, ...points] = input;
points = points.map((point) => new Point(point));
let maxArea = 0;
for (let i = 0; i < N - 2; i++) {
  for (let j = i + 1; j < N - 1; j++) {
    for (let k = j + 1; k < N; k++) {
      const A = points[i];
      const B = points[j];
      const C = points[k];
      maxArea = Math.max(maxArea, calArea(A, B, C));
    }
  }
}

console.log(maxArea);
