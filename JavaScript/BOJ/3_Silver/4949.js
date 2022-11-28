let fs = require("fs");
let input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../test.txt")
  .toString()
  .trim()
  .split("\n");

input.pop();

const check = (txt) => {
  const stack = [];
  for (let i = 0; i < txt.length; i++) {
    const t = txt[i];
    if (t === "(" || t === "[") {
      stack.push(t);
    } else if (t === ")") {
      if (!stack || stack.pop() !== "(") return false;
    } else if (t === "]") {
      if (!stack || stack.pop() !== "[") return false;
    }
  }

  if (stack.length > 0) return false;
  return true;
};

let result = "";
for (let txt of input) {
  result += (check(txt) ? "yes" : "no") + `\n`;
}
console.log(result);
