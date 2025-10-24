# 수박수박수박수박수박수?

# 1. 내 풀이
def solution(n):
    result = ""
    
    for i in range(n):
        if i % 2 == 0:
            result += '수'
        else:
            result += '박'
    
    return result

# 2. 축약형
def solution(n):
    return ('수박' * n)[:n] # '수박수박수박..' 문자열의 앞에서 n글자만 잘라서 반환