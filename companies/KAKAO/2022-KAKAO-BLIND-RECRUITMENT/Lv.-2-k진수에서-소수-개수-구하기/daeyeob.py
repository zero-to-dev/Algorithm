import math

# n을 k진법으로 변환
def numConversion(n,k):
    num = ""   # 진수 변환을 위해 필요한 문자열
    while (n > 0):
        num += str(n % k)   # 등장한 나머지순으로 변환된 숫자 뒤에서부터 들어감
        n //= k
    return "".join(reversed(num))   # 진수 변환한 숫자

# 소수 찾기
def findPrimNum(n):
    print("n:",n, "제곱근:",int(math.sqrt(n)))
    if n == 1:
        return False   # 1은 소수가 아님
    # 제곱근까지만 확인하면 1과 자기자신을 제외한 약수가 존재하는지 판별할 수 있다
    for i in range(2, int(math.sqrt(n)) + 1):      # 2부터 x의 제곱근까지의 모든 수를 확인하며
        if n % i == 0:          # x가 해당 수로 나누어떨어진다면
            return False  # 소수가 아님
    return True  # 소수임

def solution(n,k):
    result = 0
    conversionNum = numConversion(n,k)
    nonZero = conversionNum.split('0')   # 0을 기준으로 숫자 분할
    for num in nonZero:
        if num == '': continue
        else:
            if findPrimNum(int(num)):
                result += 1
    return result