# 두 수의 나눗셈

# 1 (2번보다 처리 시간 더 빠름)
def solution(num1, num2):
    return int((num1/num2) * 1000)

# 2 (나))
def solution(num1, num2):
    return ((num1/num2) * 1000) // 1

# 3 Trunc(버림)
import math

def solution(num1, num2):
    return math.trunc(num1/num2 * 1000)
