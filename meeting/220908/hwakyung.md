# 220908 카카오코테 해설

## 내가 푼 코드 설명

- 아이디어 : 차 번호를 키, {입차, 출차, 분 단위 결과} 에 대한 정보를 딕셔너리 설정한 뒤 이용하여 접근
  1. 차 정보를 담은 딕셔너리 생성
  2. records를 반복문으로 하여 각 입출차 정보 입력
  3. 그 다음 record_dict 딕셔너리 반복문을 통해 입출차 정보에 따른 분 계산
  4. change 함수 안에서 분 처리
  5. 다만 출차 정보가 23:59일 경우, 별도 out에 추가되지 않기 때문에 in의 길이만큼 반복
  6. 만일 in의 리스트 길이가 out 리스트 길이보다 길 때는 출차 정보(23:59)이 있다는 뜻
  7. 별도 계산 후, 만일 in의 분 보다 out의 분보다 클 때 out의 시간에서 1을 빼 60만큼  out의 분에 추가
  8. 그 다음 분 계산
  9. 차번호를 오름차순으로 순서대로 금액을 보여주기 위해 sorting
  10. sorting된 딕셔너리는 리스트 반환하여 각 요소는 튜플형식으로 변환
  11. 각각의 요소 중 result를 이용하여 요금 계산
  12. 만일 기본 시간 보다 더 많이 이용 시, 기본 시간 + 나머지 시간을 계산 및 반환
  13. 반환된 결과값은 answer append 및 return
```python
import math
def change(records):
    result = 0
    for idx in range(len(records['in'])):
        if len(records['out'])-1  < idx:
            out_hour,out_mins = 23,59
        else :
            out_hour,out_mins = map(int,records['out'][idx].split(":"))
        # 만약 in의 mins 값이 더 크면 out hour에서 하나 빼고 mins에 추가
        in_hour, in_mins = map(int,records['in'][idx].split(":"))

        if in_mins > out_mins:
            out_hour -= 1
            out_mins += 60

        hour = (out_hour-in_hour) * 60
        min = out_mins-in_mins
        result += hour + min
    return result

def calculated_cost(mins):
    global fees
    cost = fees[1]
    if mins > fees[0]:
        cost += math.ceil((mins - fees[0])/fees[2])*fees[3]
    return cost

def solution(fees, records):
    answer = []
    record_dict = {}
    for record in records:
        time, car_number, history = record.split(' ')
        if car_number  not in record_dict:
            record_dict[car_number] = {'in':[],"out":[],'result':0}
        record_dict[car_number][history.lower()].append(time)

    for car in record_dict:
        time_caculate = change(record_dict[car])
        record_dict[car]['result'] = time_caculate

    record_dict= sorted(record_dict.items())
    for car in record_dict:
        cost= calculated_cost(car[1]['result'])
        answer.append(cost)

    return answer
```

## 내가 뽑은 베스트 코드
- 종혁님 코드를 베스트 코드로 선정
- 다른 분들도 다 잘 푸셨지만 메서드를 잘 활용한 점이 인상 깊었습니다. :)
- 더불어 본격적인 문제 풀이 전 조건과 어떻게 풀 것인지 자세히 적어둔 것을 보고 배울 점이 많았습니다! 
```javascript

const solution = (fees, records) => {
  const cars = {};

  records.forEach((v) => {
    let [time, car, type] = v.split(' ');

    const [hour, minute] = time.split(':'); //시간 및 분 분리

    time = hour * 60 + Number(minute); // 분으로 변환

    if (!cars[car]) {
      cars[car] = { time: 0, car }; // 만약 기존 차량 정보가 없다면 생성
    }

    cars[car].type = type; # in or out 지정

    if (type === 'OUT') {
      cars[car].time += time - cars[car].lastInTime; // 출차면 입차 시기과 계산
      return;
    }

    cars[car].lastInTime = time;
  });

  return Object.values(cars)
    .sort((a, b) => a.car - b.car) # 정렬
    .map((v) => {
      if (v.type === 'IN') { //입차는 있는데 출차는 없다면
        v.time += 1439 - v.lastInTime;//23:59 계산
      }

      if (fees[0] > v.time) { // 기본 시간만 사용했다면
        return fees[1]; // 기본 요금만
      }

      return fees[1] + Math.ceil((v.time - fees[0]) / fees[2]) * fees[3]; //기본 시간 초과로 사용할시 값 계산
    });
};
```
- 

## 프로그래머스에서 가장 높은 추천을 받은 코드
- defaultdict() : 딕셔너리를 만드는 dict 클래스의 서브클래스
  - defaultdict() 인자로 주어진 객체의 기본값을 딕셔너리값의 초기값으로 지정
1. 선언된 Parking 클래스 생성 
2. 시간, 차번호, 입출차에 대한 정보를 바탕으로 값 업데이트
3. 차번호 기준으로 정렬 후, 계산
```python
from collections import defaultdict
from math import ceil

class Parking:
    def __init__(self, fees): # 기본 클래스 생성
        self.fees = fees
        self.in_flag = False
        self.in_time = 0
        self.total = 0

    def update(self, t, inout): # 값 업데이트
        self.in_flag = True if inout=='IN' else False # 만약 입차면 true 아니면 false
        if self.in_flag:  self.in_time = str2int(t) #입차면 시간계산해서 넣어주기
        else:             self.total  += (str2int(t)-self.in_time) # 출차면 시간계산 및 입차 시간에서 빼기 한뒤 total에 추가

    def calc_fee(self): # 계산
        if self.in_flag: self.update('23:59', 'out')  # 만역 입차면(출차에 대한 계산 x) -> 출차 23:59 꺼 계산
        add_t = self.total - self.fees[0] # 전체 값에서 기본 요금 빼기
        return self.fees[1] + ceil(add_t/self.fees[2]) * self.fees[3] if add_t >= 0 else self.fees[1] #요금 계산

def str2int(string): # 시간계산
    return int(string[:2])*60 + int(string[3:])

def solution(fees, records):
    recordsDict = defaultdict(lambda:Parking(fees))
    for rcd in records:
        t, car, inout = rcd.split()
        recordsDict[car].update(t, inout) # 각 값에 대해 업데이트
    
    return [v.calc_fee() for k, v in sorted(recordsDict.items())]
```