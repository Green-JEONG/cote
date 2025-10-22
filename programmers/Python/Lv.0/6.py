# 몫 구하기

# 1 (권장)
def solution(num1, num2):
    return num1//num2

# 2. int() 변환
def solution(num1, num2):
    return int(num1/num2)

# 3. floor(내림): 인자의 값을 내려 정수로 반환
import math

def solution(num1, num2):
    return math.floor(num1/num2)

# 4. divmod: 몫과 나머지 동시에 구하기
def solution(num1, num2):
    return divmod(num1, num2)[0]
    '''
    num1, num2 = divmod(num1, num2)
    return num1
    '''

# 4
solution = lambda num1, num2 : num1//num2

# 5. 내장 메서드 직접 바인딩
solution = int.__floordiv__
# int.__floordiv__: 정수형에 대한 // 연산 메서드
# solution(a, b)를 그대로  a//b처럼 계산