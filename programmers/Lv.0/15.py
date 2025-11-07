# 피자 나눠 먹기 (1)

# 1
def solution(n):
    if n%7 <= 0:
        return n//7
    elif n%7 > 0:
        return n//7 + 1
    
# 2. 올림(ceil, X)
import math
def solution(n):
    return math.ceil(n/7)

# 3 (올림과 비슷, 앞에 여유 더해주는 방식)
def solution(n):
    return (n+6) // 7 # n을 7로 나눴을 때 나머지가 있으면 올림

# 4 (올림과 비슷, 뒤에서 보정 해주는 방식)
def solution(n):
    return (n - 1) // 7 + 1 # 7로 나누어 떨어지는 경우 방지위해 미리 한칸 줄이기 + 1 더해서 올림

