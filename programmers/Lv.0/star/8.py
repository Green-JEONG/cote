# 두 수의 합 구하기

# 1
def solution(num1, num2):
    return num1+num2

# 2. 람다: *x는 함수로 들어오는 인수를 튜플로 패킹
solution = lambda * x: sum(x)