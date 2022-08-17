const fs = require("fs");
// const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
const input = fs.readFileSync("../test.txt").toString().trim().split("\n");

const [N, K] = input[0].split(" ");
const scores = input[1].split(" ");

scores.map((score) => parseInt(score));
scores.sort((a, b) => b - a);

console.log(scores[parseInt(K) - 1]);
