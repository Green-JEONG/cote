# [PCCE 기출문제] 2번 / 피타고라스의 정리

# 1
a = int(input())
c = int(input())

b_square = c**2 - a**2 # b_sqare = b**2
print(b_square)

# 2
a = int(input())
c = int(input())

b_square = pow(c, 2) - pow(a, 2) # 파이썬 내장 함수 pow(x, y): x의 y제곱 구하기
print(b_square)