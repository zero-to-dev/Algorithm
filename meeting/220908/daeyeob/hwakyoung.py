from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1]
    max_gap = -1  # 점수차

    # 중복 조합으로 0~10점까지 n개 뽑기
    for combination in combinations_with_replacement(range(11), n):
        lion_list = [0] * 11  # 라이언의 과녁 점수
        print(combination)
        # combination에 해당하는 화살들을 라이언 과녁 점수에 넣기
        for i in combination:  # 중복조합으로 나오는 점수를 담은 튜플에서 앞에서부터 하나씩 점수 체킹
            lion_list[10 - i] += 1   # 튜플에는 점수가 내림차순으로 배열 & 해당 점수칸에 적중횟수 1증가
        lion, peach = 0, 0

        # 라이언과 어피치 점수칸별 비교(10점 -> .. -> 0점)
        for idx in range(11):
            # 라이언과 어피치 모두 한번도 화살을 맞히지 못하는 경우
            if info[idx] == 0 and lion_list[idx] == 0:
                continue  # 아래 코드를 실행하지 않고 건너뜀
            # 라이언이 어피치가 쏜 화살의 수 이상을 맞힌 경우
            elif lion_list[idx] > info[idx]:
                lion += 10 - idx   # 라이언이 해당 점수 가져감
            # 어피치가 라이언보다 많은 수의 화살을 맞힌 경우
            elif lion_list[idx] <= info[idx]:
                peach += 10 - idx   # 어피치가 해당 점수 가져감

        # 라이언의 점수가  더 높은 경우
        if lion > peach:
            # 기존보다 더 큰 점수차인 경우
            if lion - peach > max_gap:
                max_gap = lion - peach   # 최대 점수차 갱신
                answer = lion_list   # 이때의 라이언의 점수 리스트를 정답으로 갱신

    return answer

print("1번 케이스:", solution(5,[2,1,1,1,0,0,0,0,0,0,0]))  # [0,2,2,0,1,0,0,0,0,0,0]
print("2번 케이스:", solution(5,[2,1,1,1,0,0,0,0,0,0,0]))   # [-1]
print("3번 케이스", solution(5,[0,0,1,2,0,1,1,1,1,1,1]))  # [1,1,2,0,1,2,2,0,0,0,0]
print("4번 케이스", solution(10,[0,0,0,0,0,0,0,0,3,4,3]))   # [1,1,1,1,1,1,1,1,0,0,2]