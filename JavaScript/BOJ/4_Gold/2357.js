const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../test.txt")
  .toString()
  .trim()
  .split("\n");

class SegmentTree {
  constructor(N, cal) {
    const segN = 1 << (Math.ceil(Math.log2(N)) + 1);
    this.N = N;
    this.tree = new Array(segN).fill(-cal(1000000000, -1000000000));
    this.cal = cal;
  }

  init(nums, node = 1, s = 0, e = this.N) {
    if (s == e) return (this.tree[node] = nums[s]);
    const mid = (s + e) >> 1;
    return (this.tree[node] = this.cal(this.init(nums, node << 1, s, mid), this.init(nums, (node << 1) + 1, mid + 1, e)));
  }

  getNum(a, b, node = 1, s = 0, e = this.N) {
    if (s > b || e < a) return -this.cal(1000000000, -1000000000);
    if (a <= s && e <= b) return this.tree[node];

    const mid = (s + e) >> 1;
    return this.cal(this.getNum(a, b, node << 1, s, mid), this.getNum(a, b, (node << 1) + 1, mid + 1, e));
  }
}

const [N, M] = input[0].split(" ").map((n) => parseInt(n));
const nums = [];
for (let i = 1; i < N + 1; i++) nums.push(parseInt(input[i]));

const minNums = new SegmentTree(N, Math.min);
const maxNums = new SegmentTree(N, Math.max);

minNums.init(nums);
maxNums.init(nums);

let result = "";
for (let i = N + 1; i < N + M + 1; i++) {
  const [a, b] = input[i].split(" ").map((n) => parseInt(n) - 1);
  result += `${minNums.getNum(a, b)} ${maxNums.getNum(a, b)}\n`;
}

console.log(result);
