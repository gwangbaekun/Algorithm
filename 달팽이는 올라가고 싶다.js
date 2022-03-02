const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `2 1 5`
).split(" ");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let up = parseInt(input([0]));
let down = parseInt(input([1]));
let height = parseInt(input([2]));

console.log(Math.ceil((height - up) / (up - down)) + 1);
