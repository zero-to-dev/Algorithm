from collections import deque
def solution(rc, operations):
    l = len(rc)
    row = deque(deque(i[1:-1]) for i in rc)
    col = [deque(rc[i][0] for i in range(l)), deque([rc[i][len(rc[0])-1] for i in range(l)])]
    for i in operations:
        if i[0] == "S":
            if len(row) != 0:
                row.appendleft(row.pop())
            col[0].appendleft(col[0].pop())
            col[1].appendleft(col[1].pop())
        else:
            if len(row) != 0:
                row[l-1].append(col[1].pop())
            col[0].append(row[l-1].popleft())
            row[0].appendleft(col[0].popleft())
            col[1].appendleft(row[0].pop())

    answer = []
    for i in range(l):
        answer.append([])
        answer[i].append(col[0][i])
        answer[i].extend(row[i])
        answer[i].append(col[1][i])
    return answer