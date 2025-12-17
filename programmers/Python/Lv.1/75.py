# 삼총사

# 1. 내풀이
from itertools import combinations

def solution(number):
    nums = []
    
    for i in combinations(number, 3):
        nums.append(sum(i))
        
    return nums.count(0)

# 2. 더 효율적이고 깔끔하게 (불필요한 리스트 제거)
from itertools import combinations

def solution(number):
    cnt = 0

    for i in combinations(number, 3):
        if sum(i) == 0:
            cnt += 1

    return cnt