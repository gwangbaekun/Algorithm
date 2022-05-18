const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let N = input();

const xMove = [0, 0, -1, 1];
const yMove = [1, -1, 0, 0];

const main = () => {
  let pic = [];
  for (let i = 0; i < N; i++) {
    pic.push(input());
  }
  let picrow = pic[0].length;
  while (true) {
    for (let i = 0; i < picrow; i++) {
        
    }
  }
};
