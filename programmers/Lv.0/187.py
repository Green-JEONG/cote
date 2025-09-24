# 홀짝에 따라 다른 값 반환하기

# 1
def solution(n):
    total = 0
    if n % 2: # 홀수 판별 공식
        for i in range(1, n+1, 2):
            total += i
    else:
        for i in range(2, n+1, 2):
            total += i**2
    return total

# 2
def solution(n):
    return (
        sum(i for i in range(1, n+1, 2))
        if n%2 != 0
        else sum(i**2 for i in range(2, n+1, 2))
    )

# 3
def solution(n):
    if n % 2: # 홀수라면
        # return sum(i for i in range(1, n+1, 2))
        return sum(range(1, n+1, 2))
    else: # 짝수라면
        return sum(i**2 for i in range(2, n+1, 2))