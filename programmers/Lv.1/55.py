# 두 개 뽑아서 더하기

# 1. 내 풀이
from itertools import combinations

def solution(numbers):
    result = set()

    for i in combinations(numbers, 2):
        result.add(sum(i))

    return sorted(result)

# 2. 이중 for문 활용 (조합 X)
def solution(numbers):
    result = set()
    n = len(numbers)

    for i in range(n-1): # i+1부터 비교할 거라 마지막은 비교 대상 X
        for j in range(i+1, n):
            result.add(numbers[i] + numbers[j])

    return sorted(result)