row_count = 0
column_count = 0
operations_count = {'ShiftRow': 0, 'Rotate': 0}
rcs = []
repetition_count = 0

first_row = [''] * column_count
right_column = [''] * (row_count - 2)
last_row_reverse = [''] * column_count
left_column_reverse = [''] * (row_count - 2)


def findCoord(count):
    global repetition_count
    pure_count = count % repetition_count
    # first_row에 넣는다
    if 0 <= pure_count < column_count:
        return [pure_count, 0]
    # right_column에 넣는다
    elif column_count <= pure_count < column_count + (row_count - 2):
        return [column_count - 1, pure_count - column_count + 1]
    # last_row_reverse에 넣는다
    elif column_count + (row_count - 2) <= pure_count < column_count * 2 + (row_count - 2):
        return [pure_count - column_count - row_count + 2, row_count - 1]
    # left_column_reverse에 넣는다
    else:  # column_count*2 + (row_count - 2)*2
        return [0, pure_count - column_count - row_count - count + 3]


def makeRotate(count):
    global rcs, repetition_count, first_row, right_column, last_row_reverse, left_column_reverse
    pure_count = count % repetition_count
    first_row = [''] * column_count
    right_column = [''] * (row_count - 2)
    last_row_reverse = [''] * column_count
    left_column_reverse = [''] * (row_count - 2)
    for index in range(repetition_count):
        target_index = pure_count + index

    # 첫번째와 마지막 row를 직접 만든다
    # 중간 row들은 맨 앞 뒤 element만 변경한다
    # 이후 rcs의 첫번째와 마지막 row를 교체한다 얕은 복사로 넣는다!

    # 교체 후 초기화
    first_row = [''] * column_count
    right_column = [''] * (row_count - 2)
    last_row_reverse = [''] * column_count
    left_column_reverse = [''] * (row_count - 2)


def makeShiftRow(count):
    global rcs
    pure_count = count % row_count
    rcs = rcs[-pure_count:] + rcs[:pure_count - 1]


def solution(rc, operations):
    global row_count, column_count, operations_count, rcs, repetition_count
    rcs = rc
    row_count = len(rcs)  # 전역 변수 변경
    column_count = len(rcs[0])  # 전역 변수 변경
    repetition_count = row_count * 2 + column_count * 2 - 4
    last_operation = "ShiftRow"
    for index in range(len(operations)):
        current_operation = operations[index]
        if last_operation == current_operation:
            operations_count[current_operation] += 1
            pass
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
    # 남은 operation 처리하기
    if last_operation == "ShiftRow":
        makeShiftRow(operations_count[last_operation])
    else:
        makeRotate(operations_count[last_operation])
    return rcs
