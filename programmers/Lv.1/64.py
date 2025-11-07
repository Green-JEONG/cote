# 없는 숫자 더하기

# 1. 내 풀이
def solution(numbers):
    total = 0
    
    for i in range(10):
        if i not in numbers:
            total += i
            
    return total

# 2. 수학적으로 간결하게 표현
def solution(numbers):
    # 0부터 9까지 합은 45
    return 45 - sum(numbers)