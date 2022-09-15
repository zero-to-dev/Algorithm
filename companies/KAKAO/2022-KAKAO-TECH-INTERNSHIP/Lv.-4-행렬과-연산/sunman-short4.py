from collections import deque

def solution(rc, operations):
    left = deque([r[0] for r in rc])
    right = deque([r[-1] for r in rc])
    body = deque([deque(r[1:-1]) for r in rc])
    for op in operations:
        if op == "Rotate":
            body[0].appendleft(left.popleft())
            right.appendleft(body[0].pop())
            body[-1].append(right.pop())
            left.append(body[-1].popleft())
        elif op == "ShiftRow":
            left.appendleft(left.pop())
            right.appendleft(right.pop())
            body.appendleft(body.pop())
    answer = list([left[r]] + list(body[r]) + [right[r]] for r in range(len(rc)))
    return answer