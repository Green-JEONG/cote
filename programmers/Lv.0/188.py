# 공배수

# 1
def solution(number, n, m):
    return 1 if number % n == 0 and number % m == 0 else 0

# 2
def solution(number, n, m):
    return int(number % n == 0 and number % m == 0)

# 3
def solution(number, n, m):
    return int(not(number % n) and not(number % m)) # not 두 조건에 모두 줘야 함!