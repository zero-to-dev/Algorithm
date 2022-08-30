# 220830

## K진수에서 소수 개수 구하기(python)

### 풀이

- 진수 변환 후, 0으로 split된 결과값에 대해 소수 판별하여 count

```python
import string
import math

temp = string.digits + string.ascii_lowercase
def convert(num,base): # 진수 변환
    q,r = divmod(num,base)
    if q ==0:
        return temp[r]
    else:
        return convert(q,base) + temp[r]

def is_Prime(num): # 소수 판별
    for n in range(2,int(math.sqrt(num))+1):
        if num%n == 0:
            return False
    return True

def solution(n, k):
    result = convert(n,k)
    number_list = result.split('0')
    count = 0
    for n in number_list:
        if n != "" and int(n) > 1:
            if is_Prime(int(n)) :
                count += 1

    return count
```
