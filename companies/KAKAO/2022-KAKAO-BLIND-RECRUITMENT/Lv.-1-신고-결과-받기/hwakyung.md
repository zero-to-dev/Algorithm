# 220829

## 신고 결과 받기 (python)

### 풀이

- 딕셔너리 생성하여 키, 값 설정 및 정리

```python
def solution(id_list, reports, k):
    id_info = {} # 유저 정보
    count_info = {} # 카운트 정보
    for id in id_list:
        id_info[id] = [0, []]
        count_info[id] = 0

    for report in reports:
        reporter, reported_user = report.split(" ")
        if reporter not in id_info[reported_user][1]: # 중복 추가 막기
            id_info[reported_user][0] += 1 # 신고 카운트
            id_info[reported_user][1].append(reporter) # 해당 유저를 신고한 유저 추가

    for id in id_info:
        if id_info[id][0] >=k: # k 값 이상으로 신고가 되었으면
            for user in id_info[id][1]:
                count_info[user] += 1 # 카운트 추가
    return list(count_info.values())

```
