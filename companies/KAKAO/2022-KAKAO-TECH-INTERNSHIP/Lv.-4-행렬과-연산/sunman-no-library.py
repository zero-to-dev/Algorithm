'''
돌리기와 비끼기 두 가지 종류의 연산을 한다.
2차원 배열을 다음과 같이 쪼개자.
왼쪽열, 오른쪽열, 나머지를 위에서부터 행별로 쪼갠다.
1. shiftrow
start_ 값들이 변하는 것으로 끝. 1만큼 감소한다.
2. rotate
left의 경우 start_left 값이 1만큼 증가.
left_top(top의 좌표는 start_left에 의해 저장)의 값을 임시저장.
기존 top의 좌표에 새로 들어오는 값-아랫줄의 두 번째 값을 넣는다.
이는 M=2 일 경우에는 right_bottom, 아니면 rows[아랫줄][0]에서 구할 수 있다.
rows[아랫줄]의 경우, start_ 위치의 값을 right_bottom값을 가져와준다.
이후 start_의 값을 1 증가시켜준다.
비슷하게 우측과 상단에 대해서도 실시해준다.
'''

def solution(rc, operations):
    left = [r[0] for r in rc]
    right = [r[-1] for r in rc]
    N = len(rc)
    M = len(rc[0])
    rows = [[row[i] for i in range(1,M-1)] for row in rc]
    L = len(rows[0])


    start_left = 0
    start_right = 0
    start_rows = 0
    zero_rows = [0] * N



    for oper in operations:
        if oper[0] == "R":
            start_rows %= N
            start_left %= N
            start_right %= N
            temp = left[start_left]
            if L > 0:

                left[start_left] = rows[start_rows-1][zero_rows[start_rows-1]]

                start_left += 1
                start_left %= N

                rows[start_rows-1][zero_rows[start_rows-1]] = right[start_right-1]
                zero_rows[start_rows-1] += 1
                zero_rows[start_rows-1] %= L

                right[start_right - 1] = rows[start_rows][zero_rows[start_rows]-1]
                start_right -= 1
                start_right %= N

                rows[start_rows][zero_rows[start_rows]-1] = temp
                zero_rows[start_rows] -= 1
                zero_rows[start_rows] %= L


            else:
                left[start_left] = right[start_right-1]
                start_left += 1
                start_left %= N

                start_right -= 1
                start_right %= N
                right[start_right] = temp

        else:
            start_rows -= 1
            start_left -= 1
            start_right -= 1



    answer = []
    for i in range(N):
        answer.append([left[(start_left+i)%N]])

        row_id = (start_rows+i)%N
        row = rows[row_id]
        zero_id = zero_rows[row_id]
        for j in range(L):
            answer[-1].append(row[(zero_id+j)%L])
        answer[-1].append(right[(start_right+i)%N])


    return answer