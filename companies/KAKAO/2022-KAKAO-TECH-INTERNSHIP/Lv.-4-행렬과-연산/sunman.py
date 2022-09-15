row_count = 0
column_count = 0
operations_count = {'ShiftRow': 0, 'Rotate': 0}
rcs = []
repetition_count = 0

def findCoord(count):
    global repetition_count
    pure_count = count % repetition_count
    # 맨 윗줄
    if 0 <= pure_count < column_count:
        return [pure_count, 0]
    # 맨 오른줄
    elif column_count <= pure_count < column_count + (row_count - 1):
        return [column_count - 1, pure_count - (column_count - 1)]
    # 맨 아래줄
    elif column_count + (row_count - 1) <= pure_count < column_count * 2 + (row_count - 2):
        return [column_count - 1 - (pure_count - (column_count - 1 + row_count - 1)), row_count - 1]
    # 맨 왼줄
    else:  # column_count*2 + (row_count - 2)*2
        return [0, row_count - 1 - (pure_count - (column_count - 1 + row_count - 1 + column_count - 1))]


def makeRotate(count):
    global rcs, repetition_count
    pure_count = count % repetition_count
    temp_copy_stack = []

    for index in range(repetition_count):
        # [0,0] 부터 시작하여 시계방향으로 원소를 뽑아 stack에 넣는다
        [x, y] = findCoord(index)
        temp_copy_stack.append(rcs[y][x])

    for index in range(repetition_count):
        # 뽑아 만든 stack을 순서대로 추출하여 n 만큼 회전한 곳에 붙여넣는다.
        target_index = pure_count + index
        [x, y] = findCoord(target_index)
        rcs[y][x] = temp_copy_stack[index]


def makeShiftRow(count):
    global rcs
    pure_count = count % row_count
    if (pure_count):
        rcs = rcs[-pure_count:] + rcs[:row_count - (pure_count)]


def solution(rc, operations):
    global row_count, column_count, operations_count, rcs, repetition_count
    rcs = rc
    row_count = len(rcs)
    column_count = len(rcs[0])
    repetition_count = row_count * 2 + column_count * 2 - 4
    last_operation = "ShiftRow"
    for index in range(len(operations)):
        current_operation = operations[index]
        if last_operation == current_operation:
            operations_count[current_operation] += 1
        else:
            # 다르다면 이전까지 있었던 operation을 그 횟수에 맞게 먼저 수행
            if last_operation == "ShiftRow":
                makeShiftRow(operations_count[last_operation])
            else:
                makeRotate(operations_count[last_operation])
            # 기존 operation_count 초기화
            operations_count[last_operation] = 0
            # 새 operation_count = 1
            operations_count[current_operation] = 1
            # 새 operation을 기록
            last_operation = current_operation

    # 혹시나 잔여 operation이 있다면 처리
    if (operations_count['Rotate']):
        makeRotate(operations_count[last_operation])
    if (operations_count['ShiftRow']):
        makeShiftRow(operations_count[last_operation])
    return rcs


# print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"]))
# print('------------ real anwer ------------')
# print([[8, 9, 6], [4, 1, 2], [7, 5, 3]])


# print(solution([[8, 6, 3], [3, 3, 7], [8, 4, 9]],["Rotate", "ShiftRow", "ShiftRow"]))
# print('------------ real anwer ------------')
# print([[8, 3, 3], [4, 9, 7], [3, 8, 6]])


# print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]))
# print('------------ real anwer ------------')
# print([[1, 6, 7 ,8], [5, 9, 10, 4], [2, 3, 12, 11]])
