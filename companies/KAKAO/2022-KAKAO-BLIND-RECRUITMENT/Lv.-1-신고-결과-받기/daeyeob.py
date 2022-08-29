def solution(id_list, report, k):   # 신고자 리스트, 신고자&피신고자 리스트, 신고 기준 횟수
    mail_list = [0 for _ in range(len(id_list))]   # 신고 처리 결과 받는 메일리스트
    report_dict = {id: 0 for id in id_list}   # 신고당한 아이디: 신고 당한 횟수
    report = set(report)   # 중복 제거

    for who in report: report_dict[who.split(' ')[1]] += 1

    for who in report:
        if report_dict[who.split(' ')[1]] >= k:   # k번 이상 신고가 확인 되었을 경우
            idx = id_list.index(who.split(' ')[0])
            mail_list[idx] += 1   # 해당 신고자는 신고 성공

    return 