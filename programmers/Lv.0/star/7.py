# 몫 구하기

# 1
def solution(num1, num2):
    return num1//num2

# 2
def solution(num1, num2):
    return int(num1/num2)

# 3. floor(내림): 인자의 값을 내려 정수로 반환
import math

def solution(num1, num2):
    return math.floor(num1/num2)

# 4
def solution(num1, num2):
    return divmod(num1, num2)[0]
    '''
    num1, num2 = divmod(num1, num2)
    return num1
    '''

# 4
solution = lambda num1, num2 : num1//num2

# 5
solution = int.__floordiv__