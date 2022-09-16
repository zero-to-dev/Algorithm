from collections import deque


def solution(queue1, queue2):
    deque1 = deque(queue1)
    deque2 = deque(queue2)
    cnt = 0
    max_cnt = len(deque1) * 3
    sum1, sum2 = sum(deque1), sum(deque2)
    
    while (deque1 and deque2) and max_cnt != cnt:
        if sum1 == sum2:
            return cnt
        
        elif sum1 < sum2:
            temp = deque2.popleft()
            deque1.append(temp) 
            sum1 += temp
            sum2 -= temp
        else:
            temp = deque1.popleft()
            deque2.append(temp)
            sum2 += temp
            sum1 -= temp
        cnt += 1
    return -1
    
    