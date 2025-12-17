# 크기가 작은 부분 문자열

# 1. 문자 3개씩 묶는 슬라이싱 범위 조정 똑바로
def solution(t, p):
    length = len(p)
    cnt = 0

    for i in range(len(t) - length+1): # i는 0부터 len(t) - length 까지만 돌아야 함
        num = int(t[i:i+length])
        
        if num <= int(p):
            cnt += 1
            
    return cnt

# 2. 변수 하나 더 안 세우고 더 간단히
def solution(t, p):
    length = len(p)
    cnt = 0

    for i in range(len(t) - length+1):
        if int(t[i:i+length]) <= int(p):
            cnt += 1

    return cnt