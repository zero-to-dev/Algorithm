### 코드

```python
from collections import deque


def bfs(n, info):
    queue = deque()
    queue.append((0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    res_list = []
    max_difference = 0

    # 명심할 것: 나 어피치 아니고 내가 저번대회 우승자 라이언임

    while queue:
        cur_point, cur_status = queue.popleft()

        # 종료 조건 1:
        # 화살 다 쏘면 어피치 - 라이언 포인트 비교
        if sum(cur_status) == n:
            apeach = 0
            lion = 0

            # 10포인트 ~ 0포인트까지 돌면서 어피치와 내 포인트를 비교
            # 라이언이 어피치보다 더 많이 맞춘 경우에만, 해당 포인트만큼 라이언 점수에 추가
            # 라이언과 어피치가 동일한 화살의 개수만큼 하나의 포인트에 맞췄거나, 어피치가 더 많이 맞춘 경우에는
            # 해당 포인트만큼 어피치 점수에 추가
            # 전적으로 라이언이 억울한 게임임
            for i in range(11):
                if not (info[i] == 0 and cur_status[i] == 0):
                    if cur_status[i] > info[i]:
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

        # 종료 조건 2:
        # 어피치랑 나랑 같은 개수의 화살을 쏴야하기 때문에
        # 만약에 내가 쏜 화살의 개수의 총합가 어피치가 쏜 n 발을 넘어간다?
        # 그런 상황이 아예 불가이기에 무시해버리기
        elif sum(cur_status) > n:
            continue

        # 종료 조건 3:
        # 고득점 포인트에서 다 화살 못 쏘고 0점까지 오게되었다면, 유감입니다만
        # 0점에라도 화살을 다 쏴서 남은 화살 소진시켜야 함
        elif cur_point == 10:
            case_c = cur_status[:]
            case_c[10] = n - sum(cur_status)
            queue.append((-1, case_c))

        # 이제서야 등장하는 메인 상황(??)
        # 선택할 수 있는 2가지 옵션:
        # 1) 어피치가 해당 포인트에 쏜 점수보다 1점 더 많이 쏜다
        # 2) 아예 해당 포인트에는 화살을 쏘지 않는다
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

    # res_return: 최대 점수차로 어피치를 이길 수 있는 점수 배열
    # 1. 빈 배열이면, 어피치를 이길 수 없다는 것
    # 2. 1이면 최대 점수차를 낼 수 있는 경우의 수가 1개이므로 그것을 그대로 출력
    # (단, 배열안에 배열이 들어있는 상황이기에 res_return 이 아닌, res_return[1] 을 반환해야 함)
    # 3. 배열의 길이가 2보다 크면, 가장 낮은 점수를 더 맞힌 경우를 반환
    if res_return:
        if len(res_return) == 1:
            return res_return[0]
        else:
            return res_return[-1]
    else:
        return [-1]
```

### 아이디어

- 코드 사이사이에 주석으로 적어놓는 게 더 보기 편할까 싶어서, 그렇게 적어봤습니다.

- copy 대신에 [:] 을 이용해서 배열을 복사해줬습니다 ㅋㅋ 

### 느낀점

- 와 확실히 어렵고 제가 풀었던 여태까지의 문제들과 다른 느낌을 받았습니다.
- bfs를 이렇게도 쓸 수 있구나 되게 놀랐던 문제였습니다.
- 이런 차원에서 더욱이 다양한 문제를 접해서 실력을 키워야 겠구나 싶었습니다! 
