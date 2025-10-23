# 두 정수 사이의 합

# 1. 내 풀이
def solution(a, b):
    total = 0
    
    if a <= b:
        for n in range(a, b+1):
            total += n
    else:
        for n in range(b, a+1):
            total += n
        
    return total

# 2. 더 간결한 방법
def solution(a, b):
    total = 0

    for n in range(min(a, b), max(a, b)+1):
        total += n
    
    return total
    # return sum(range(min(a, b), max(a, b)+1))