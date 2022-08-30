/**
 * 미지의 것 : 양의 정수 n을 k 진수로 바꿨을 때, 변환된 수 안에 아래 조건에 맞는 소수가 몇 개인가
 *          1. 0P0처럼 소수 양쪽에 0이 있는 경우
 *          2. P0처럼 소수 오른쪽에만 0이 있고 왼쪽에는 아무것도 없는경우
 *          3. 0P처럼 소수 왼쪽에만 0이 있고 오른쪽에는 아무것도 없는 경우
 *          4. P처럼 소수 양쪽에 아무것도 없는 경우
 * 자료
 * - P는 각 자릿수에 0을 포함하지 않는 소수
 *    - 101은 P가 될 수 없다.
 * - 437674를 3진수로 바꾸면 '211' 0 '2' 01010 '11' 이다.
 *    - 소수는 왼쪽부터 순서대로 211 2 11이 있다.
 * - 수를 k진법으로 보았을 때가 아닌, 10진법으로 보았을 때 소수여야 한다.
 *
 * 조건
 * - P는 각 자릿수에 0을 포함하지 않는 소수이다.
 *    - '101'은 P가 될 수 없다.
 *
 * 계획
 * - transition 변수를 선언한다.
 * - transition에 n.toString(k)를 하여 진법 변환을 한 값을 할당한다.
 * - transition을 하나씩 더하며 10진법으로 변환했을 때, 소수이면
 *    - 해당 수에 0이 포함되어있는지 확인하고 0이 없다면 count++를 한다.
 *
 * 반성
 * - 0이 있으면의 조건을 인지하고 있었음에도 split을 쓸 생각조차 하지 못했습니다. (자료에 넣지 못했습니다.)
 * - 주어진 자료를 파악할 때, 주어진 조건의 본질을 파악해야겠다는 생각이 들었습니다.
 * - 문제를 너무 어렵게 생각하는 것도 문제인 것 같습니다.
 */

const isPrime = (number) => {
  const integerNumber = Number(number);

  if (integerNumber <= 1) return false;

  for (let i = 2; i < Math.sqrt(integerNumber + 1); i += 1) {
    if (integerNumber % i === 0) return false;
  }

  return true;
};

// const solution = (n, k) => {
//   const transition = n.toString(k);
//   const targets = [];

//   let target = '';
//   for (let i = 0; i < transition.length; i += 1) {
//     if (transition[i] !== '0') {
//       target += transition[i];
//     } else {
//       target = '';
//     }
//     if (transition[i + 1] === '0' || transition[i + 1] === undefined) {
//       if (isPrimeAndNotIncludeZero(target)) {
//         targets.push(target);
//         target = '';
//       }
//     }
//   }

//   const setTargets = new Set(targets);

//   return [...setTargets].length;
// };

const solution = (n, k) => {
  const numbers = n.toString(k).split('0');

  return numbers.filter((number) => number !== '' && isPrime(number)).length;
};

describe('k진수에서 소수 개수 구하기', () => {
  it('소수 개수를 구합니다.', () => {
    expect(solution(437674, 3)).toBe(3);
    expect(solution(110011, 10)).toBe(2);
  });

  it('소수면서 0을 포함하고 있지 않은지 확인합니다.', () => {
    expect(isPrime(1)).toBe(false);
    expect(isPrime(2)).toBe(true);
    expect(isPrime(3)).toBe(true);
    expect(isPrime(11)).toBe(true);
    expect(isPrime(7)).toBe(true);
  });
});
