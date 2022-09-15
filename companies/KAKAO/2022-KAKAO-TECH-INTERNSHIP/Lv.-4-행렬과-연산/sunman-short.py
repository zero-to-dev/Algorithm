from collections import deque

def solution(rc, operations):
    answer = []

    c1 = deque([(i, 0) for i in range(len(rc))])
    c2 = deque([(i, len(rc[0]) - 1) for i in range(len(rc))])
    r = deque([deque([(i, j) for j in range(1, len(rc[0]) - 1)]) for i in range(len(rc))])

    for op in operations:
        if op == 'Rotate':
            r[0].appendleft(c1.popleft())
            c2.appendleft(r[0].pop())
            r[-1].append(c2.pop())
            c1.append(r[-1].popleft())
        else:
            c1.appendleft(c1.pop())
            c2.appendleft(c2.pop())
            r.appendleft(r.pop())

    for i in range(len(rc)):
        tmp = []
        tmp.append(rc[c1[i][0]][c1[i][1]])
        for x, y in r[i]:
            tmp.append(rc[x][y])
        tmp.append(rc[c2[i][0]][c2[i][1]])
        answer.append(tmp)

    return answer