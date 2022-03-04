const fs = require("fs");
const { endianness } = require("os");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `1 16`
).split(" ");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let M = parseInt(input());
let N = parseInt(input());

let arr = Array(N + 1).fill(true);
arr[0] = false;
arr[1] = false;

for (let i = 2; i * i <= N; i++) {
  if (arr[i]) {
    for (let j = i * i; j <= N; j += i) {
      arr[j] = false;
    }
  }
}

for (let i = M; i <= N; i++) {
  if (arr[i] == true) {
    console.log(i);
  }
}
