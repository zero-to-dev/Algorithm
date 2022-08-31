# 220829

## 주차 요금(python)

### 풀이

- 자동차 입출차 정보를 저장할 딕셔너리 생성
  - 자동차 번호가 키
  - 입차, 출차, 총 시간(분 단위)를 값으로 설정
  - 딕셔너리 값 = in : [] out : [], time: int
- 해당 딕셔너리에 대한 in, out을 리스트를 반복문으로 하여 시간 변환(분 단위로)
  - 만일 출차의 분 단위가 입차의 분 단위 보다 작으면 출차의 시간에서 1 제거 및 출차의 분에 60 추가
- 총 계산된 분을 가지고 요금 계산
  - 기본 시간 초과 시, 기본 시간을 제한 나머지 시간에 단위 시간 및 요금 곱하기(분 단위)

```python
import math
def time_calculator(record): # 분 단위 계산 함수
    result = 0
    for idx in range(len(record['in'])):
        if len(record['out'])-1  < idx: # 출차 시간에 대한 정보가 없는 경우
            out_hour,out_mins = 23,59 # 23:59 분에 나간 것으로 체크
        else :
            out_hour,out_mins = map(int,record['out'][idx].split(":"))
        # 만약 in의 mins 값이 더 크면 출차의 hour에서 1 빼고 출차의 mins에 추가
        in_hour, in_mins = map(int,record['in'][idx].split(":"))

        if in_mins > out_mins:
            out_hour -= 1
            out_mins += 60

        hour = (out_hour-in_hour) * 60
        min = out_mins-in_mins
        result += hour + min
    return result

def cost_calculator(mins,fees): # 비용 계산 함수
    cost = fees[1]
    if mins > fees[0]: # 기본 시간 초과 시
        cost += math.ceil((mins - fees[0])/fees[2])*fees[3]
    return cost

def solution(fees, records):
    answer = []
    record_dict = {} # 기록을 위한 record 딕셔너리
    for record in records:
        time, car_number, history = record.split(' ')
        if car_number  not in record_dict: # 만약 이전에 차번호가 추가되어 있지 않다면
            record_dict[car_number] = {'in':[],"out":[],'result':0}
        record_dict[car_number][history.lower()].append(time)

    for record in record_dict:
        time_result = time_calculator(record_dict[record]) # 시간을 분 단위로 계산
        record_dict[record]['result'] = time_result # 해당 결과값 record 딕셔너리에 넣어주기
    # 차 번호 오름차순으로 표시하기 위해 정렬
    record_dict= sorted(record_dict.items())

    for record in record_dict:
        cost= cost_calculator(record[1]['result'],fees)
        answer.append(cost) # 결과 append

    return answer
```
