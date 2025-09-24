# 두 수의 합 구하기

# 1 (권장)
def solution(num1, num2):
    return num1+num2

# 2. 람다: *x는 함수로 들어오는 인수를 튜플로 패킹 (여러개 일때 유용)
solution = lambda * x: sum(x)
# *x: 인수 모두 모아 하나의 튜플에 담음(패킹)