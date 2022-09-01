# 220901

## 양궁대회 (python)

### 풀이

- 문제 풀이 실패
  - 조합을 이용한 아이디어를 참고하여 풀이
- 초기 재귀함수를 이용하여 문제를 풀었으나 모든 케이스를 보지 못했거나 뒤에서부터 채워나가는 형식으로 다시 풀기 도전

```python
from itertools import combinations_with_replacement

def solution(n,info):
    answer = [-1]
    max_gap = -1

    for combination in combinations_with_replacement(range(11),n):
        lion_list = [0] * 11

        for i in combination:
            lion_list[10 - i] +=1
        lion,peach = 0,0
        for idx in range(11):
            if info[idx] == 0 and lion_list[idx] == 0:
                continue
            elif lion_list[idx] > info[idx]:
                lion += 10-idx
            elif lion_list[idx] <= info[idx]:
                peach += 10-idx

        if lion > peach:
            if lion-peach > max_gap:
                max_gap = lion-peach
                answer = lion_list

    return answer

```
