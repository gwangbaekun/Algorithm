const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

[a, b] = input().split(" ");
let A = parseInt(a); // 가로
let B = parseInt(b); // 세로
const arrs = [];
for (let i = 0; i < B; i++) {
  arrs.push(
    input()
      .split(" ")
      .map((el) => parseInt(el))
  );
}

// 1일차
function day(arr) {
  let _arrs = arr;
  for (let i = 0; i < B; i++) {
    for (let j = 0; j < A; j++) {
      if (_arrs[i][j] == 1) {
        if (i > 0) _arrs[i - 1][j] = 1;
        if (i < B - 1) _arrs[i + 1][j] = 1;
        if (j > 0) _arrs[i][j - 1] = 1;
        if (j < A - 1) _arrs[i][j + 1] = 1;
      }
    }
  }
  return (arr = _arrs);
}

function check(arr) {
  let count = 0;
  let _arr = arr;
  for (let i = 0; i < B; i++) {
    for (let j = 0; j < A; j++) {
      if (_arr[i][j] === 0) {
        if (i === 0 || arr[i - 1][j] === -1) {
          if (i === B - 1 || arr[i + 1][j] === -1) {
            if (j === 0 || arr[i][j - 1] === -1) {
              if (j === A - 1 || arr[i][j + 1] === -1) {
                return -1;
              }
            }
          }
        }
      }
      if (_arr[i][j] === 1 || _arr[i][j] === -1) {
        count++;
      }
    }
  }
  if (count === A * B) {
    return 1;
  }
  return 0;
}

let dayCount = 0;
for (let i = 0; i < B; i++) {
  for (let j = 0; j < A; j++) {
    if (!check(arrs) === 1) {
      day(arrs);
      dayCount++;
    }
    if (check(arrs) === 1 || check(arrs) === -1) {
      if (check(arrs) === -1) {
        dayCount = -1;
      }
      break;
    }
  }
}

console.log(dayCount);

function (element) {
  if (element == 3) {
    return True
  }
}