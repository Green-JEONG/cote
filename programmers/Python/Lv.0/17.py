# 피자 나눠 먹기 (3)

# 1. (직관적이지만 긴 코드)
def solution(slice, n):
    return n // slice + 1 if n % slice > 0 else n // slice
    
    # return n // slice + (1 if n % slice else 0) # 나머지가 있으면 1 더하고, 없으면 그대로

# 2 n-1로 한 칸 밀어놓으면, 몫만 계산해도 올림 처리 (생각 필요)
def solution(slice, n):
    return ((n-1) // slice) + 1

# 3 (파이써닉)
def solution(slice, n):
    d, m = divmod(n, slice)
    return d + int(m != 0) # 나머지가 0이 아니면 1(True) 더하기

# 4. 수학적(올림, 가장 직관적)
from math import ceil
def solution(slice, n):
    return ceil(n / slice)

# 5. 올림 나눗셈의 정석
def solution(slice, n):
    return (n + slice - 1) // slice

# 6. 불리언 (True = 1, False = 0)
def solution(slice, n):
    return n // slice + (n % slice > 0)

# 7. 음수 나눗셈 (트릭)
def solution(slice, n):
    return -(-n // slice) # 파이썬에서 음수 나눗셈은 내림이 아닌 작은 쪽(더 음수)로 내려감 -> 그래서 올림 효과(음수 부호 두 번 사용해서 정수 올림 나눗셈)