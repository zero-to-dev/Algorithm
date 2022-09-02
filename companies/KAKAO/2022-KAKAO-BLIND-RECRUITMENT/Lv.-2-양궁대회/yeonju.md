### 코드

```python
from collections import deque


def bfs(n, info):
    queue = deque()
    queue.append((0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    res_list = []
    max_difference = 0

    while queue:
        cur_point, cur_status = queue.popleft()

        if sum(cur_status) == n:
            apeach = 0
            lion = 0

            for i in range(11):
                if not (info[i] == 0 and cur_status[i] == 0):
                    if cur_status[i] >= info[i]:
                        lion += (10 - i)
                    else:
                        apeach += (10 - i)

            if lion > apeach:
                difference = lion - apeach

                if difference < max_difference:
                    continue
                if difference > max_difference:
                    max_difference = difference
                    res_list = []
                res_list.append(cur_status)

        elif sum(cur_status) > n:
            continue

        elif cur_point == 10:
            case_c = cur_status[:]
            case_c[10] = n - sum(cur_status)
            queue.append((-1, case_c))

        else:
            case_a = cur_status[:]
            case_b = cur_status[:]

            case_a[cur_point] = info[cur_point] + 1
            case_b[cur_point] = 0

            queue.append((cur_point + 1, case_a))
            queue.append((cur_point + 1, case_b))

    return res_list


def solution(n, info):
    res_return = bfs(n, info)

    if res_return:
        if len(res_return) == 1:
            return res_return[0]
        else:
            return res_return[-1]
    else:
        return [-1]

```