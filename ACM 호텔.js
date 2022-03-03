const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `2
50 50 457
3 40 28`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let line = parseInt(input());

while (line) {
  let temp = input([line]).split(" ");
  let H = parseInt(temp[0]);
  let W = parseInt(temp[1]);
  let N = parseInt(temp[2]);

  if (N % H === 0) {
    if (N / H < 10) {
      console.log(H + "0" + N / H);
    } else {
      console.log(String(H) + N / H);
    }
  } else {
    if (N / H < 9) {
      console.log(String(N % H) + "0" + Math.ceil(N / H));
    } else {
      console.log(String(N % H) + Math.ceil(N / H));
    }
  }

  line -= 1;
}
