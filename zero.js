const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `10
1
3
5
4
0
0
7
0
0
6`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let temp = input();
let arr = [];
for (let i = 0; i < temp; i++) {
  let j = input();
  if (j === "0") {
    arr.pop();
  } else {
    arr.push(j);
  }
}
let answer = 0;
let length = arr.length;

for (let i = 0; i < length; i++) {
  answer += parseInt(arr[i]);
}

console.log(answer);
