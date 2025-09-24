# 편지

# 1 (권장)
def solution(message):
    return len(message)*2

# 2. 비트 연산: 왼쪽 시프트, 2의 거듭제곱 배 곱하기, x<<1과 x*2이 동일 (트릭, 잘 안쓰임)
def solution(message):
    return len(message)<<1 # len(message) * (2**1) = len(message)*2
