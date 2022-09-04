### 코드

```python
from collections import defaultdict


def solution(fees, records):
    temp = []
    ans = []

    def calculate_time():
        in_time = defaultdict(int)
        out_time = defaultdict(int)

        for record in records:
            time, car, inout = record.split()
            hour, min = time.split(':')
            calculated_mins = int(hour) * 60 + int(min)

            if inout == 'IN':
                in_time[car] = calculated_mins

            elif inout == 'OUT':
                out_time[car] += calculated_mins - in_time[car]
                del in_time[car]

        for car, minutes in in_time.items():
            out_time[car] += 23 * 60 + 59 - minutes

        ordered_li = sorted(out_time.items())

        for each in ordered_li:
            temp.append(each[1])

    def calculate_cost(times):
        for time in times:
            if time <= fees[0]:
                ans.append(fees[1])
            else:
                cost = fees[1]
                time -= fees[0]

                cost += (time // fees[2]) * fees[3]

                if time % fees[2] != 0:
                    cost += fees[3]
                ans.append(cost)

    calculate_time()
    calculate_cost(temp)

    return ans


```

### 문제 요약

- 차량이 출차된 내역 없으면 23:59에 출차
- 기본 시간 이하: 기본 요금
- 기본 시간 초과: 기본 요금 + 초과한 시간에 단위 시간마다 단위 요금
    - 단위시간으로 나눠 떨어지지 않으면 올림
- return 값: 차량 번호가 작은 자동차부터 값을 정수 배열에 담기

### 아이디어

- 깔끔해 보이는 게 좋아서, 함수 2개 만들었습니다.
    - calculate_time(): 차가 총 머문 시간 계산하는 함수
    - calculate_cost(): 한 개의 차가 내야할 비용 계산하는 함수

- calculate_time() 함수 안에 in_time 과 out_time 이라는 디폴트 딕셔너리를 만들었습니다. (기본 value 값은 int 0으로 설정한 딕셔너리)
    - out_time 에 해당 차가 주차장에 머문 누적 시간을 관리할 것임  
    - 차가 주차장에 들어왔으면 in_time 에 삽입
    - 차가 주차장에서 나가면 out_time - in_time 연산으로 몇 분동안 있었나 확인 
        - 참고로 차가 입차 - 출차 후 또 다시 주차장에 올 수 있기에 값은 덮어씌워주는 것이 아닌 시간 추가 후 업데이트를 해줘야 합니다.
        - 덧붙여, 해당 시간 계산 후에는 in_time 딕셔너리에서 해당 key-value 묶음을 없애줘야 합니다. (23:59까지 머물렀던 차가 있나 확인하기 위한 장치)
    - 다 돌았는데, in_time 에 자동차 정보가 남아있으면 해당 차가 23:59까지 머물렀다는 것을 의미합니다. 그렇기에 23:59 - in_time 을 해줘서 주차장에서 머문 시간을 추가해줍니다. 

- calculate_cost() 를 통해 해당 차가 지불해야할 금액을 계산해줍니다. 
    1)  기본 시간 이하로 머물렀다? 기본 요금만 낸다
    2) 기본 시간을 초과해서 머물렀다? 
        (머문 시간 - 기본 시간) 을 계산한 후 남은 시간을 단위 시간으로 나눠줌
        - i) 값이 0으로 나눠 떨어지면 딱 단위시간만큼 주차한 것
        - ii) 값이 0으로 나눠 떨어지지 않으면 단위 시간 1 unit 만큼 더 청구해야 함
        ```
        e.g.)
        문제에서 주어진 요금표를 기준으로 191분 머물렀다면, 
        180분은 기본 요금을 냄
        나머지 11분 (= 191분 - 180분) 은 추가 요금으로 계산
        10분 + 1분 <- 19분 머물던 거랑 다를 바 없음
        그치만 어쩌겠어.. 
        ```

- 귀찮게시리,,, 문제에서 차량 번호가 작은 자동차부터 청구할 금액을 정수 배열에 담아 제출하라고 했습니다. 그렇기 때문에 calculate_time() 에서 calculate_cost() 로 넘어가는 중간에 딕셔너리의 값들을 사건순으로 오름차순 정렬시켜주는 것도 잊지 말야아 합니다. 

- defaultdict 라이브러리가 정말 편한 게, 딕셔너리에 키 값이 없어도 값 추가할 때 딱히 제약 사항이 없습니다. 키가 있나 없나 확인할 필요 없이 그냥 넣기만 하면 됩니다. 이거 진짜 왕강추