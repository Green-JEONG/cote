# 배열 만들기 1

# 1. 조건문 사용
def solution(n, k):
    return [x for x in range(1, n+1) if x % k == 0]

# 2. 배수 활용
def solution(n, k):
    return [x for x in range(k, n + 1, k)]