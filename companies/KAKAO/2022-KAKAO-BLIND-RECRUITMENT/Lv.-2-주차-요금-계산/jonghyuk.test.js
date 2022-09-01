/* eslint-disable prefer-const */
/* eslint-disable prefer-destructuring */
/* eslint-disable no-unused-expressions */
/* eslint-disable consistent-return */
/**
 * 미지의 것 : 청구할 주차 요금
 *
 * 자료
 * - 차량이 입차된 후에 출차된 내역이 없다면, 23:59에 출차된 것으로 간주
 *
 * - !!입차 후 출차 내역이 없다면 { 기본요금 + [(누적 주차 시간 - 기본 시간) / 10] * 단위 요금!!
 * - 하루에 두 번, 주차장을 이용하는 경우 누적 주차 시간을 더한다. (기본 요금을 두 번 내지 않는다.)
 *
 * - 00:00부터 23:59까지의 입/출차 내역을 바탕으로 차량별 누적 주차 시간을 계산하여 요금을 "일괄"로 정산
 * - 누적 주차 시간이 기본 시간 이하라면
 *    - 기본 요금 청구
 * - 누적 주차 시간이 기본 시간을 초과하면
 *    - 초과시간 + 단위 시간(요금)
 *        - 초과한 시간이 단위 시간으로 나뉘지 않으면 올림함
 * - 주차 요금 : fees[] : int
 * - 입/출차 내역 : records[] : string
 *
 *
 *
 * 조건
 * - 주차장에 없는 차량은 출차되지 않는다.
 * - 주차장에 이미 있는 차량이 입차되지 않는다.
 * - 같은 시각에, 같은 차량번호의 내역이 2번 이상 나타나지 않는다.
 *
 * ## 계획
 * - 배열을 각자 분리한다. o
 * - 차량 번호를 key로 하는 object를 만든다. o
 * - 누적 시간을 (분)으로 계산한다
 * - 반복문을 돌며 object[key] = 누적 시간 += 누적시간을 한다
 * - 계산함수 => 기본 요금 + [(누적 주차 시간 - 기본 시간) / 10] * 단위 요금 함수를 만든다.
 * - 반복문이 끝나면 요금을 계산한다.
 *
 *
 * 반성
 */

const solution = (fees, records) => {
  const cars = {};

  records.forEach((v) => {
    let [time, car, type] = v.split(' ');

    const [hour, minute] = time.split(':');

    time = hour * 60 + Number(minute);

    if (!cars[car]) {
      cars[car] = { time: 0, car };
    }

    cars[car].type = type;

    if (type === 'OUT') {
      cars[car].time += time - cars[car].lastInTime;
      return;
    }

    cars[car].lastInTime = time;
  });

  return Object.values(cars)
    .sort((a, b) => a.car - b.car)
    .map((v) => {
      if (v.type === 'IN') {
        v.time += 1439 - v.lastInTime;
      }

      if (fees[0] > v.time) {
        return fees[1];
      }

      return fees[1] + Math.ceil((v.time - fees[0]) / fees[2]) * fees[3];
    });
};

describe('주차 요금 계산', () => {
  it('주차 요금이 배열에 담겨 반환됩니다.', () => {
    expect(
      solution(
        [180, 5000, 10, 600],
        [
          '05:34 5961 IN',
          '06:00 0000 IN',
          '06:34 0000 OUT',
          '07:59 5961 OUT',
          '07:59 0148 IN',
          '18:59 0000 IN',
          '19:09 0148 OUT',
          '22:59 5961 IN',
          '23:00 5961 OUT',
        ],
      ),
    ).toEqual([14600, 34400, 5000]);
  });
});
