# 최대공약수와 최소공배수

# 1. 내 풀이
import math

def solution(n, m):
    gcd = math.gcd(n, m)
    lcm = 0
    
    i = max(n, m)
    while True:
        if i % n == 0 and i % m == 0:
            lcm = i
            break
        else:
            i += 1
    
    return [gcd, lcm]

# 2. 최적 코드
import math

def solution(n, m):
    gcd = math.gcd(n, m)
    lcm = (n * m) // gcd # 최소공배수 = 두 수 곱한 수를 최대공약수로 나누기

    return [gcd, lcm]