const fs = require("fs");
const stdin = (
  process.platform === "linux" ? fs.readFileSync("/dev/stdin").toString() : `0`
).split(" ");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let temp = parseInt(input());
// console.log(temp);
let count = 0;
let newNum = parseInt(temp);

while (newNum || newNum === 0) {
  if (newNum < 10) {
    newNum = parseInt(String(newNum) + String(newNum));
  } else {
    newNum = parseInt(
      String(newNum % 10) +
        String((Math.floor(newNum / 10) + (newNum % 10)) % 10)
    );
  }
  count += 1;
  // console.log(newNum);
  if (newNum == parseInt(temp)) {
    console.log(count);
    break;
  }
}
