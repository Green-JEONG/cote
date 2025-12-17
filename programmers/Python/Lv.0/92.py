# 세균 증식

# 1 (권장)
def solution(n, t):
    return n * (2**t)

# 2 (t가 커지면 비효율적)
def solution(n, t):
    for _ in range(t):
        n *= 2
    return n

# 3. 비트 연산: 왼쪽 시프트 (n을 2**t배하는 것과 동일, 빠르지만 직관적 X)
def solution(n, t):
    return n << t # n * (2**t)