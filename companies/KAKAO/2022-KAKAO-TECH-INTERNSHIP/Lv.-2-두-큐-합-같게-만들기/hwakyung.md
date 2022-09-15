# 20220915 두 큐 합 같게 만들기

### 풀이
- 제한 시간으로 deque 사용
- sum 함수가 생각보다 퍼포먼스에 영향을 많이 끼치기 때문에 사용을 자제해야 함
```python
from collections import deque
def solution(queue1, queue2):
    answer = 0
    length = len(queue1)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    qOne = sum(queue1)
    qTwo = sum(queue2)

    for i in range(length*3):
        if qOne == qTwo:
            break
        elif qOne > qTwo:
           qOne -=  queue1[0]
           qTwo += queue1[0]
           queue2.append(queue1.popleft(0))
        elif qOne < qTwo:
            qOne += queue2[0]
            qTwo -= queue2[0]
            queue1.append(queue2.popleft(0))
        answer += 1

    if answer > length*3:
        answer = -1

    return answer
```