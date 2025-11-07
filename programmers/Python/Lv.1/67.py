# 내적

# 1. 내 풀이
def solution(a, b):
    total = 0
    
    for i in range(len(a)):
        total += a[i]*b[i]
        
    return total

# 2. zip 함수 활용
def solution(a, b):
    total = 0

    for x, y in zip(a, b):
        total += x * y

    return total