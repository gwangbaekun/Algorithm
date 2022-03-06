const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `3
0 0 13 40 0 37
0 0 3 0 7 3
1 1 1 1 1 5`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let temp = input();

for (let i = 0; i < temp; i++) {
  let a = input().split(" ");
  let j = Math.sqrt((a[0] - a[3]) ** 2 + (a[1] - a[4]) ** 2);
  let p = parseInt(a[2]) + parseInt(a[5]);
  let k = Math.abs(parseInt(a[2]) - parseInt(a[5]));

  if (j === 0) {
    if (k === 0) {
      console.log(-1);
    } else {
      console.log(0);
    }
  } else {
    if (j < k) {
      console.log(0);
    } else if (j == k) {
      console.log(1);
    } else if (j > k && j < p) {
      console.log(2);
    } else if (j == p) {
      console.log(1);
    } else if (j > p) {
      console.log(0);
    }
  }
}
