from collections import deque

def solution(rc, operations):
    answer = []
    rn, cn = len(rc), len(rc[0])
    rows = deque(deque(row[1:-1]) for row in rc)
    outline = [deque(rc[r][0] for r in range(rn)),
                deque(rc[r][cn - 1] for r in range(rn))]
    for operation in operations:
        if operation == "ShiftRow":
            rows.rotate(1)
            outline[0].rotate(1)
            outline[1].rotate(1)
        if operation == "Rotate":
            rows[rn-1].append(outline[1].pop())
            outline[0].append(rows[rn-1].popleft())
            rows[0].appendleft(outline[0].popleft())
            outline[1].appendleft(rows[0].pop())


    for i in range(rn):
        answer.append([])
        answer[i].append(outline[0][i])
        answer[i].extend(rows[i])
        answer[i].append(outline[1][i])

    return answer