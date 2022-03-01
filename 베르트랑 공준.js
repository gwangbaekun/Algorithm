const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `1
  10
  13
  11
  1000
  10000
  100000
  0`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const isPrime = (num) => {
  if (num === 1) {
    return false;
  }
  if (num === 2) {
    return true;
  }
  for (let i = 2; i <= Math.floor(Math.sqrt(num)); i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return true;
};

for (let i = 0; i < stdin.length; i++) {
  let count = 0;
  let temp = parseInt(input());
  if (temp === 0) {
    return null;
  } else {
    for (let j = 1; j <= 2 * temp; j++) {
      if (isPrime(j) === true) {
        count++;
      }
    }
    for (let j = 1; j <= temp; j++) {
      if (isPrime(j) === true) {
        count--;
      }
    }
  }
  console.log(count);
}
