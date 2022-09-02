### 코드
다소 급하게 풀어서 코드가 좀 복잡한데, 리팩토링해서 다시 제출하겠습니다! 

```python
from collections import defaultdict

def solution(fees, records):
    ans = []
    temp = []

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

    for car, min in in_time.items():
        out_time[car] += 23 * 60 + 59 - min

    ordered_li = sorted(out_time.items())

    for each in ordered_li:
        temp.append(each[1])

    calculate_cost(temp)

    return ans

```