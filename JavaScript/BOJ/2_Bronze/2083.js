const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../test.txt")
  .toString()
  .trim()
  .split("\n");

const result = [];

for (let member of input) {
  const [name, age, height] = member.split(" ");
  if (name === "#") break;

  if (age > 17 || height >= 80) result.push(`${name} Senior`);
  else result.push(`${name} Junior`);
}

console.log(result.join("\n"));
