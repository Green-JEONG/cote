# 소수 찾기

# 1. '소수 판별 함수' 활용
def solution(n):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    
    cnt = 0
    
    for i in range(2, n+1):
        if is_prime(i):
            cnt += 1
    
    return cnt

# 2. '에라토스테네스의 체' 활용
def solution(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False

    return sum(sieve)