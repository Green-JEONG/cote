# 나머지가 1이 되는 수 찾기

# 1. 내 풀이
def solution(n):
    result = []
    
    for x in range(1, n+1):
        if n % x == 1:
            result.append(x)
            
    return result[0]


# 2. 효율적으로 보다 단순화한 개선된 코드
def solution(n):
    for x in range(1, n):
        if n % x == 1:
            return x