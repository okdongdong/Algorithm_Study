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

const [NL, ...pointsInput] = input;
const [N, L] = NL.split(" ").map((n) => parseInt(n));
const points = pointsInput.map((point) => new Point(point));

function ccw(a, b, c) {
  return (b.x - a.x) * (c.y - a.y) - (c.x - a.x) * (b.y - a.y);
}

function distanceSquare(a, b) {
  return (a.x - b.x) ** 2 + (a.y - b.y) ** 2;
}

function compare(originPoint, a, b) {
  const result = ccw(originPoint, a, b);
  if (result > 0) return -1;
  if (result < 0) return 1;
  return distanceSquare(originPoint, a) < distanceSquare(originPoint, b) ? -1 : 1;
}

function solution(N, L, points) {
  points.sort((a, b) => {
    if (a.y != b.y) return a.y - b.y;
    else return a.x - b.x;
  });

  const originPoint = points[0];
  points.sort((a, b) => compare(originPoint, a, b));

  const convexHull = [];

  for (let point of points) {
    while (convexHull.length >= 2 && ccw(convexHull[convexHull.length - 2], convexHull[convexHull.length - 1], point) <= 0) {
      convexHull.pop();
    }
    convexHull.push(point);
  }

  // 외각의 크기의 합은 항상 360도
  const cornerLength = 2 * Math.PI * L;
  let edgeLength = 0;
  convexHull.push(convexHull[0]);
  for (let i = 1; i < convexHull.length; i++) {
    edgeLength += Math.sqrt(distanceSquare(convexHull[i], convexHull[i - 1]));
  }
  const wallLength = Math.round(edgeLength + cornerLength);
  return wallLength;
}

console.log(solution(N, L, points));
