let expression = "100-200*300-500+20";
// + - *
// + * -
// - + *
// - * +
// * + -
// * - +

function solution(expression) {
  let answer_list = [];
  answer_list.push(Math.abs(minus_plus_multiply(expression)));
  answer_list.push(Math.abs(plus_minus_multiply(expression)));
  answer_list.push(Math.abs(minus_multiply_plus(expression)));
  answer_list.push(Math.abs(multiply_minus_plus(expression)));
  answer_list.push(Math.abs(multiply_plus_minus(expression)));
  answer_list.push(Math.abs(plus_multiply_minus(expression)));
  return answer_list.reduce((acc, cur) => {
    return cur - acc > 0 ? cur : acc;
  });
}

function minus_plus_multiply(expression) {
  // - + *
  let _expression = expression.split("*");
  let before_expression = [];
  for (let i = 0; i < _expression.length; i++) {
    let answer_minus = [];
    let __expression = _expression[i].split("+");
    for (let j = 0; j < __expression.length; j++) {
      // - 연산 먼저
      answer_minus.push(minus(__expression[j].split("-")));
    }
    before_expression.push(plus(answer_minus));
  }
  return multiply(before_expression);
  // - 로 나눔
}

function plus_minus_multiply(expression) {
  let _expression = expression.split("*");
  let before_expression = [];
  for (let i = 0; i < _expression.length; i++) {
    let answer_plus = [];
    let __expression = _expression[i].split("-");
    for (let j = 0; j < __expression.length; j++) {
      answer_plus.push(plus(__expression[j].split("+")));
    }
    before_expression.push(minus(answer_plus));
  }
  return multiply(before_expression);
}
function minus_multiply_plus(expression) {
  let _expression = expression.split("+");
  let before_expression = [];
  for (let i = 0; i < _expression.length; i++) {
    let answer_plus = [];
    let __expression = _expression[i].split("*");
    for (let j = 0; j < __expression.length; j++) {
      answer_plus.push(minus(__expression[j].split("-")));
    }
    before_expression.push(multiply(answer_plus));
  }
  return plus(before_expression);
}
function multiply_minus_plus(expression) {
  let _expression = expression.split("+");
  let before_expression = [];
  for (let i = 0; i < _expression.length; i++) {
    let answer_plus = [];
    let __expression = _expression[i].split("-");
    for (let j = 0; j < __expression.length; j++) {
      answer_plus.push(multiply(__expression[j].split("*")));
    }
    before_expression.push(minus(answer_plus));
  }
  return plus(before_expression);
}
function multiply_plus_minus(expression) {
  let _expression = expression.split("-");
  let before_expression = [];
  for (let i = 0; i < _expression.length; i++) {
    let answer_plus = [];
    let __expression = _expression[i].split("+");
    for (let j = 0; j < __expression.length; j++) {
      answer_plus.push(multiply(__expression[j].split("*")));
    }
    before_expression.push(plus(answer_plus));
  }
  return minus(before_expression);
}
function plus_multiply_minus(expression) {
  let _expression = expression.split("-");
  let before_expression = [];
  for (let i = 0; i < _expression.length; i++) {
    let answer_plus = [];
    let __expression = _expression[i].split("*");
    for (let j = 0; j < __expression.length; j++) {
      answer_plus.push(plus(__expression[j].split("+")));
    }
    before_expression.push(multiply(answer_plus));
  }
  return minus(before_expression);
}

function minus(element) {
  let answer = parseInt(element[0]);
  for (let i = 1; i < element.length; i++) {
    answer -= parseInt(element[i]);
  }
  return answer;
}

element = ["200", "300"];

function plus(element) {
  let answer = parseInt(element[0]);
  for (let i = 1; i < element.length; i++) {
    answer += parseInt(element[i]);
  }
  return answer;
}

function multiply(element) {
  let answer = parseInt(element[0]);
  for (let i = 1; i < element.length; i++) {
    answer *= parseInt(element[i]);
  }
  return answer;
}

console.log(solution(expression));
