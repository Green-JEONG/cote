# [PCCE 기출문제] 3번 / 수 나누기

number = int(input())

answer = 0

for i in range(1):
    answer += number % 100
    number //= 100

print(answer)