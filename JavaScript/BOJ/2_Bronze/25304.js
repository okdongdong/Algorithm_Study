const fs = require("fs");
// const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
const input = fs.readFileSync("../test.txt").toString().trim().split("\n");
const X = parseInt(input[0]);
const N = parseInt(input[1]);
const items = input.slice(2);

let totalPrice = 0;
for (item of items) {
  const [a, b] = item.split(" ");
  totalPrice += parseInt(a) * parseInt(b);
}

if (totalPrice === X) console.log("Yes");
else console.log("No");
