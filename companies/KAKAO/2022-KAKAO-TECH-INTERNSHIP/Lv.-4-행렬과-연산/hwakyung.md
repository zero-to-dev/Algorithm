# 20220918 코딩테스트공부하기

```python
from collections import deque


def solution(rc, operations):
    row_length, column_length = len(rc), len(rc[0])
    
    # ShiftRow 연산을 위해 행별로 관리 [양쪽 원소를 제외한 행들, ...]
    rows = deque(deque(row[1:-1]) for row in rc)
    # Rotate 연산을 위해 바깥쪽 원소들(열별)을 관리 [첫열, 마지막열]
    out_columns = [deque(rc[r][0] for r in range(row_length)),
                deque(rc[r][column_length - 1] for r in range(row_length))]

    # 연산
    for operation in operations:
        # ShiftRow 연산
        if operation[0] == "S":
            # 마지막(가장 아래) 행을 처음(가장 위)로 이동
            rows.appendleft(rows.pop())
            # 첫 열과 마지막 열의 마지막(가장 아래) 원소를 처음(가장 위)으로 이동
            out_columns[0].appendleft(out_columns[0].pop())
            out_columns[1].appendleft(out_columns[1].pop())
        
        # Rotate 연산
        else:
            rows[row_length - 1].append(out_columns[1].pop())
            out_columns[0].append(rows[row_length - 1].popleft())
            rows[0].appendleft(out_columns[0].popleft())
            out_columns[1].appendleft(rows[0].pop())
            
    
    answer = []
    for r in range(row_length):
        answer.append([])
        answer[r].append(out_columns[0][r])
        answer[r].extend(rows[r])
        answer[r].append(out_columns[1][r]) 
    
    return answer
```