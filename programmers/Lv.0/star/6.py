# 두 수의 나눗셈

# 1 (2번보다 처리 시간 더 빠름, 권장)
def solution(num1, num2):
    return int((num1/num2) * 1000)

# 2 (정수 나눗셈으로 버림)
def solution(num1, num2):
    return ((num1/num2) * 1000) // 1

# 3 trunc(버림)
import math

def solution(num1, num2):
    return math.trunc(num1/num2 * 1000)
