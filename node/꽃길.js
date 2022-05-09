const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `6
1 0 2 3 3 4
1 1 1 1 1 1
0 0 1 1 1 1
3 9 9 0 1 99
9 11 3 1 0 3
12 3 0 0 0 1
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const column = parseInt(input());

const arr = [];
for (let i = 0; i < column; i++) {
  arr.push(input().split(" "));
}

const priceArr = [];
let obj = new Object();
for (let i = 1; i < column - 1; i++) {
  for (let j = 1; j < column - 1; j++) {
    const priceForOne =
      parseInt(arr[i][j]) +
      parseInt(arr[i][j + 1]) +
      parseInt(arr[i][j - 1]) +
      parseInt(arr[i - 1][j]) +
      parseInt(arr[i + 1][j]);
    const key = String(i) + String(j);
    obj[key] = priceForOne;
  }
}
// console.log(obj);

for (var key in obj) {
  priceArr.push([key, obj[key]]);
}

let min = Infinity;

for (let i = 0; i < priceArr.length; i++) {
  for (let j = 0; j < priceArr.length; j++) {
    for (let k = 0; k < priceArr.length; k++) {
      if (isPossible(priceArr[i][0], priceArr[j][0], priceArr[k][0])) {
        let temp = priceArr[i][1] + priceArr[j][1] + priceArr[k][1];
        if (temp < min) {
          min = temp;
        }
      }
    }
  }
}

console.log(min);

// 만약 22 -> 11, 33, 24, 20

function isPossible(x, y, z) {
  let X = parseInt(x);
  let Y = parseInt(y);
  let Z = parseInt(z);
  if (X - Y >= -11 && X - Y <= -9) {
    return false;
  } else if (X - Y >= -2 && X - Y <= 2) {
    return false;
  } else if (X - Y >= 9 && X - Y <= 11) {
    return false;
  } else if (Y - Z >= -11 && Y - Z <= -9) {
    return false;
  } else if (Y - Z >= -2 && Y - Z <= 2) {
    return false;
  } else if (Y - Z >= 9 && Y - Z <= 11) {
    return false;
  } else if (X - Z >= -11 && X - Z <= -9) {
    return false;
  } else if (X - Z >= -2 && X - Z <= 2) {
    return false;
  } else if (X - Z >= 9 && X - Z <= 11) {
    return false;
  } else if (X - Y === 20 || Y - X === 20) {
    return false;
  } else if (Y - Z === 20 || Z - Y === 20) {
    return false;
  } else if (X - Z === 20 || Z - X === 20) {
    return false;
  } else {
    return true;
  }
}
