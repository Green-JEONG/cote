# 두 수의 연산값 비교하기

# 1
def solution(a, b):
    return max(int(f'{a}{b}'), 2*a*b)

# 2
def solution(a, b):
    return max(int(str(a)+ str(b)), 2*a*b)