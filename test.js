const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `3
0 3
1 5
45 50`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let temp = input();

for (let i = 0; i < temp; i++) {
  let a = input().split(" ");
  let distance = a[1] - a[0];
  let sqrt = Math.floor(Math.sqrt(distance));
  if (distance > sqrt ** 2 && distance <= sqrt * (sqrt + 1)) {
    console.log(sqrt + sqrt);
  } else if (distance === sqrt ** 2) {
    console.log(2 * sqrt - 1);
  } else {
    console.log(2 * sqrt + 1);
  }
}
