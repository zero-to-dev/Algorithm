### 코드

```python
def solution(n, k):
    cnt = 0

    def to_k_num(n, k):
        temp = ''
        while n > 0:
            temp += str(n % k)
            n //= k

        return ''.join(reversed(temp))

    def is_prime(k):
        if k == 2 or k == 3:
            return True
        elif k < 2 or k % 2 == 0:
            return False
        for i in range(3, int(k ** 0.5) + 1, 2):
            if k % i == 0:
                return False

        return True

    k_num = to_k_num(n, k)
    nums = k_num.split('0')

    for check_num in nums:
        if check_num == '':
            continue
        num = is_prime(int(check_num))

        if num:
            cnt += 1

    return cnt

```