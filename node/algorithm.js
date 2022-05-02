let arr = ["a", "a", "b", "a", "c"];

const set = new Set();

set.add("a");
set.add("b");
set.add("c");

const setValue = set.values();
const setArr = [];

for (let i = 0; i < set.size; i++) {
  setArr.push(String(setValue.next().value));
}
// set arr
// const setArr = ["a","b","c"]
const arrLength = arr.length;
const setLength = setArr.length;
let answer = [];
for (let i = setLength; i < arrLength; i++) {
  for (let j = 0; j <= arrLength - setLength; j++) {
    if (j + i <= arrLength) {
      const newArr = arr.slice(j, j + i);
      if (newArr.includes("a", "b", "c")) {
        answer.push(newArr.length);
        break;
      }
    }
  }
}
console.log(answer[0]);
