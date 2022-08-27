// JS에서는 queue를 직접 구현하는 것이 shift연산보다 100배이상 빠름
class Node {
  constructor(item) {
    this.item = item;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }

  push(item) {
    const node = new Node(item);
    if (!this.head) {
      this.head = node;
      this.head.next = this.tail;
    } else {
      this.tail.next = node;
    }
    this.tail = node;
    this.size += 1;
  }

  getSize() {
    return this.size;
  }

  pop() {
    if (this.size > 2) {
      const item = this.head.item;
      const newHead = this.head.next;
      this.head = newHead;
      this.size -= 1;
      return item;
    } else if (this.size === 2) {
      const item = this.head.item;
      const newHead = this.head.next;
      this.head = newHead;
      this.tail = newHead;
      this.size -= 1;
      return item;
    } else if (this.size === 1) {
      const item = this.head.item;
      this.head = null;
      this.tail = null;
      this.size -= 1;
      return item;
    } else {
      return -1;
    }
  }

  empty() {
    return this.size ? 0 : 1;
  }

  front() {
    return this.head ? this.head.item : -1;
  }

  back() {
    return this.tail ? this.tail.item : -1;
  }
}

const fs = require("fs");
// const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const input = fs.readFileSync("../test.txt").toString().split("\n");
const [N, ...commands] = input;
const que = new Queue();
let result = "";
for (let i = 0; i < N; i++) {
  const command = commands[i].split(" ")[0];
  switch (command.trim()) {
    case "push":
      const num = parseInt(commands[i].split(" ")[1]);
      que.push(num);
      break;

    case "pop":
      result += que.pop() + "\n";
      break;

    case "size":
      result += que.getSize() + "\n";
      break;

    case "empty":
      result += que.empty() + "\n";
      break;

    case "front":
      result += que.front() + "\n";
      break;

    case "back":
      result += que.back() + "\n";
      break;
  }
}

console.log(result);
