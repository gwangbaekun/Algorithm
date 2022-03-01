const fs = require("fs");
const stdin = (
  process.platform === "linux" ? fs.readFileSync("/dev/stdin").toString() : `4`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let N = parseInt(input());
const Num = N + "";
const lastNum = parseInt(Num[Num.length - 1]);
if (lastNum == 0 || lastNum == 5) {
  console.log(N / 5);
}
if (lastNum == 3) {
  console.log((N - 3) / 5 + 1);
}
if (lastNum == 6) {
  console.log((N - 6) / 5 + 2);
}
if (lastNum == 9) {
  console.log((N - 9) / 5 + 3);
}
if (lastNum == 2) {
  console.log(N - 12 >= 0 ? (N - 12) / 5 + 4 : -1);
}
if (lastNum == 8) {
  console.log((N - 3) / 5 + 1);
}
if (lastNum == 1) {
  console.log(N - 6 >= 0 ? (N - 6) / 5 + 2 : -1);
}
if (lastNum == 4) {
  console.log(N - 9 >= 0 ? (N - 9) / 5 + 3 : -1);
}
if (lastNum == 7) {
  console.log(N - 12 >= 0 ? (N - 12) / 5 + 4 : -1);
}
