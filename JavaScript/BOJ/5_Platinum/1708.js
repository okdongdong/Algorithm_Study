// 볼록껍질

const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../test.txt")
  .toString()
  .trim()
  .split("\n");

function ccw(A, B, C) {
  const result = (B.x - A.x) * (C.y - A.y) - (C.x - A.x) * (B.y - A.y);
  return result;
}

function compare(A, B) {
  const result = ccw(ORIGIN_POINT, A, B);
  if (result > 0) return -1;
  if (result < 0) return 1;
  if (distance(ORIGIN_POINT, A) < distance(ORIGIN_POINT, B)) return -1;
  return 1;
}

function distance(A, B) {
  return (A.x - B.x) ** 2 + (A.y - B.y) ** 2;
}

class Point {
  constructor(point) {
    const [x, y] = point.split(" ").map((n) => parseInt(n));
    this.x = x;
    this.y = y;
  }
}

let [N, ...points] = input;

points = points.map((point) => new Point(point));
points.sort((a, b) => {
  if (a.y != b.y) return a.y - b.y;
  else return a.x - b.x;
});
const ORIGIN_POINT = points[0];
points.sort((a, b) => compare(a, b));

const convexHullPoints = [];

for (let point of points) {
  while (convexHullPoints.length >= 2 && ccw(convexHullPoints[convexHullPoints.length - 2], convexHullPoints[convexHullPoints.length - 1], point) <= 0)
    convexHullPoints.pop();
  convexHullPoints.push(point);
}

console.log(convexHullPoints.length);
