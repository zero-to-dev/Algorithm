# https://school.programmers.co.kr/learn/courses/30/lessons/92341
import math

# 분으로 환산하기
def calcmin(timeInfo):
    hh,mm = timeInfo.split(":")
    minute = int(hh)*60 + int(mm)   # 분으로 변환
    return minute

def solution(fees, records):
    endOfDay = 23*60 + 59   # 23시 59분
    intime = {}   # 입차 기록을 저장
    allparkingtime = {}   # 누적 주차시간 저장
    result = []   # 결과값 담음

    for record in records:
        time, carNum, inORout = record.split()

        # 들어왔을 경우
        if inORout == "IN":
            intime[carNum] = calcmin(time)   # 딕셔너리에 차번호 & 분단위로 기록
            if carNum not in allparkingtime:   # 누적 주차시간 기록에 없는 경우
                allparkingtime[carNum] = 0   # 차량번호 & 주차시간:0을 초기값으로 넣어줌

        # 나간 경우
        else:
            allparkingtime[carNum] += calcmin(time) - intime[carNum]   # 누적주차시간을 저장 (출차시간-입차시간)
            del intime[carNum]   # 출차하였으므로 입차시간 기록 제거

    # 들어오기만하고 나간 기록이 없는 케이스 확인
    for carNumber, inminutes in intime.items():
        allparkingtime[carNumber] += endOfDay - inminutes   # '23시 59분 - 들어온시간'을 누적해서 더해줌


    basic_time, basic_fee, unit_time, unit_fee = fees   # 기본시간, 기본요금, 단위시간, 단위요금
    for carNumber, parkingTime in sorted(allparkingtime.items()):   # 오름차순으로 체킹
        if parkingTime <= basic_time:   # 주차시간이 기본시간보다 적은 경우
            result.append(basic_fee)   # 기본요금만 넣어줌
        else:   # 기본시간을 초과한 경우
            result.append(basic_fee+ math.ceil((parkingTime-basic_time)/unit_time)*unit_fee)
            #  기본요금 + [(총 주차시간 - 기본시간)/단위시간]*단위요금

    return result


print(solution([180, 5000, 10, 600]	,["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591],["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10],["00:00 1234 IN"]))



'''

실패 1
# fees: 기본시간, 기본요금, 단위 시간, 단위 요금 (분,원 단위)
   # records: 시각(HH:MM), 차량번호(XXXX), 내역(IN/OUT)
   timeDic = {}
   endOfDay = 23*60+59   # (23시 59분)
   result = []
   total = collections.defaultdict(int)

   # 출차를 한 경우
   for record in records:
       times, carNum, inORout = record.split()   # 시간, 차량번호, 출입여부 분리 - split()과 split(" ")은 동일
       time = calcmin(times)   # 분으로 환산

       # 입차 여부에 따라 시간 계산
       if carNum in timeDic:   # 이미 입차되어 있는 경우
           total[carNum] += time - timeDic[carNum]
           del timeDic[carNum]
       else:   # 입차할 경우
           timeDic[carNum] = time


   # 출차를 하지 않은 경우
   for num, minutes in timeDic.items():
       total[carNum] += endOfDay - minutes

   # 요금 계산
   basic_minutes, basic_fee, unit_minutes, unit_fee = fees
   for num, t in total.items():
       cost = basic_fee
       if t > basic_minutes:   # 추가요금 발생
           cost += math.ceil((t-basic_minutes)/unit_minutes)*unit_fee  # 올림 처리
       result.append((num,cost))


   # 차량번호 오름차순
   result.sort()
   return [num[1] for num in result]

'''






''' 
실패 2

if inORout == "IN":    # 들어올시
            timeDic[carNum] = time   # 차량 번호에 해당하는 '분'을, 차량번호: 분 꼴로 저장
        else:   # 나갈시
            feeDic[carNum] = feeDic.get(carNum,0) + (time-timeDic[carNum])
            # feeDic.et(carNum,0): carNum(key)에 해당하는 요금 feeDic(value)에 없다면 디폴트값인 0을 가져옴
            del timeDic[carNum]
            # del 딕셔너리[키값] ->  지정한 키에 해당하는 {key: value}쌍 제거
            # 나간 차량 삭제

    print(feeDic)
    print(timeDic)


    # 금액 지불
    for carNum, fee in sorted(feeDic.items()):
        if fee > fees[0]:   # 기본시간보다 오래 주차한 경우
            result.append(calcFee(fee,records))   # 환산한 금액 지불
        else:   # 기본시간보다 적게 주차한 경우
            result.append(fees[1])   # 기본요금만 지불
'''