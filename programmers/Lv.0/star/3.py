# [PCCE 기출문제] 3번 / 수 나누기

number = int(input())

answer = 0

while number > 0: # 수정: 반복이 안 되어서 일반화가 불가했다. / 그냥 number도 가능: 0은 False+이외 True이므로
    answer += number % 100
    number //= 100

print(answer)