# 콜라츠 추측

# 1. 내 풀이
def solution(num):
    if num == 1:
        return 0
    
    cnt = 0
    
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1 # 계산 순서 주의
        cnt += 1

        if cnt >= 500:
            return -1
        
    return cnt

# 2. 효율적인 시간복잡도를 고려한 최적의 구조
def solution(num):
    cnt = 0
    
    for cnt in range(500):
        if num == 1:
            return cnt
        
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
    return -1