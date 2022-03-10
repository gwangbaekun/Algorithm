const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `14
push 1
push 2
top
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
top`
).split("\n");

// const input = (() => {
//   let line = 0;
//   return () => stdin[line++];
// })();

const stack = [];
const result = [];

const len = stdin.shift();

for (let i = 0; i < len; i++) {
  switch (stdin[i]) {
    case "pop":
      result.push(stack.pop() || -1);
      break;

    case "size":
      result.push(stack.length);
      break;

    case "empty":
      result.push(stack[0] ? 0 : 1);
      break;

    case "top":
      result.push(stack[stack.length - 1] || -1);
      break;

    default:
      stack.push(stdin[i].split(" ")[1]);
      break;
  }
}

console.log(result.join("\n"));
