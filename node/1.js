const fs = require("fs");
const { endianness } = require("os");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `3
11
9901`
).split("\n");

const input = (() => {
    let line = 0;
    return () => stdin[line++]
})();

for (let i = 0; i < stdin.length; i ++) {
    let num = 11
    let count = 2
    while (true) {
        if (num % parseInt(stdin[i]) === 0) {
            break;
        } else {
            num = num * 10 + 1
            count ++
        }
    }
    console.log(count)
}