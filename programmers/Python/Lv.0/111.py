# 주사위 게임 1

# 1. 내풀이
def solution(a, b):
    score = 0
    
    if a % 2 == 1 and b % 2 == 1:
        score += a**2 + b**2
    elif (a+b) % 2 == 1:
        score += 2 * (a+b)
    else:
        score += abs(a-b)
        
    return score

# 2. a와 b 중 하나만 홀수라는 의도 명확히
def solution(a, b):
    score = 0
    
    if a % 2 == 1 and b % 2 == 1:
        score += a**2 + b**2
    elif a % 2 != b % 2:
        score += 2 * (a+b)
    else:
        score += abs(a-b)
        
    return score