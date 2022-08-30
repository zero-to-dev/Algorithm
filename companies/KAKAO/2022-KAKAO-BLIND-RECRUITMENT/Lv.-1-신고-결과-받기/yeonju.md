### 코드


```python
from collections import defaultdict


def solution(id_list, report, k):

    reported_list = defaultdict(set)
    warned_list = defaultdict(int)
    email_list = []
    res = []

    for each in report:
        reported_user, warned_user = each.split(' ')
        if warned_user in reported_list[reported_user]:
            continue
        reported_list[reported_user].add(warned_user)
        warned_list[warned_user] += 1

    for each in warned_list:
        if warned_list[each] >= k:
            email_list.append(each)

    for each in id_list:
        cnt = 0
        for individual in email_list:
            if individual in reported_list[each]:
                cnt += 1
        res.append(cnt)

    return res

```



### 아이디어

*  문제에서 주어진 'report' 리스트를 [신고자, 신고 받은 사람]으로 분리하기
    1) 신고자가 같은 사람을 한 번 더 신고한 경우: 
        - 무시해버리기
    2) 신고자가 어떤 사람을 처음으로 신고하는 경우: 
        - 'reported_list'라는 딕셔너리에 담음 
        - 'warned_list'라는 딕셔너리에 신고 받은 사람의 cnt 를 1 증가

* 'report' 리스트를 싹 돌고 나서 k 이상 신고 당한 사람이 누군지 체크
  - k번 이상 신고된 사람은 'email_list'라는 리스트에 담기

* 문제에서 주어진 'id_list'의 신고자 순서에 맞게끔, 그 해당 사람한테 보내야 할 이메일 수 각각 뽑아오기
  -  'email_list'에 있는 사람이 'reported_list'의 해당되는 사람(key 값)의 value 값으로 들어있다면 그 개수만큼 추가

* 결과값을 담고 있는 'res' 라는 리스트를 그대로 리턴


### 느낀점

* 문제 풀면서 생각보다 혼란스러웠습니다.
* 내가 여태까지 무엇을 한 거지...라는 생각이 머릿속을 지배해버렸고 (ㅋㅋㅋ)
* 일단, 프로그래머스 문제 푸는 환경이 익숙하지 않았습니다.
(고수는 도구 탓을 하지 않는다만, 저는 고수가 아니니 도구 탓을 하겠습니닼ㅋㅋㅋ)
* 여태까지는 문제를 풀면서 리스트나 딕셔너리를 생성해 나갔던 경우가 많았는데, 확실히 이 문제에서는 미리 다 설계해놓고 문제를 풀어야 한다는 교훈을 배웠습니다.
* 그리고 한 문제에서 이렇게 많은 배열 혹은 딕셔너리를 만드는 경험이 좀 낯설어서, '이게 맞나?' 싶은데 리팩토링을 통해 다시 제출하겠습니다.
* 이 한 문제를 통해서 생각하게 된 것이 참 많네요... 겸손하게 열심히 해야겠다 다시 한 번 느꼈습니다!


