# 곱셈 (입출력, 사칙연산, 수학)
# 빈 칸에 들어갈 수는?

# 1. 문자열 변환
num1 = int(input())
num2 = input()

print(num1 * int(num2[2]))
print(num1 * int(num2[1]))
print(num1 * int(num2[0]))
print(num1 * int(num2))

# 2. 수학적 방법 (문자열 없이 자리수 분리)
num1 = int(input())
num2 = int(input())

print(num1 * (num2 % 10))
print(num1 * (num2 // 10 % 10))
print(num1 * (num2 // 100))
print(num1 * num2)