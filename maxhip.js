const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `13
0
1
2
0
0
3
2
1
0
0
0
0
0`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const temp = input();

let answer = [];
for (let i = 0; i < temp; i++) {
  answer.push(parseInt(input([i])));
}

console.log(answer);
