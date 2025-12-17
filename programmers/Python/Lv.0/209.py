# n의 배수

# 1
def solution(num, n):
    return 1 if num % n == 0 else 0

# 2
def solution(num, n):
    return not (num % n)

    # return int(not(num % n)) # (가장 깔끔, 무조건 정수 요구시)

    # return int(num % n == 0)
