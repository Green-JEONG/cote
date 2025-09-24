# 양꼬치

# 1
def solution(n, k):
    return n*12000 + k*2000 - (n//10)*2000

# 2 (권장)
def solution(n, k):
    return n*12000 + (k - n // 10)*2000
    # 서비스 음료 개수: n//10

# 3 (X)
def solution(n, k):
    total = n*12000 + k*2000
    total -= (n//10) * 2000
    return total