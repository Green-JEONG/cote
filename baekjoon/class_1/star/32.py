# 2675. 문자열 반복

t = int(input())
for _ in range(t):
    r, s = input().split() # map()에는 함수와 반복 가능한 객체 두 개 필요
    # r = int(r) 도 가능
    result = ""
    for i in s:
        result += i * int(r) # 문자열 누적하려면 += 연산자 쓰기
    print(result)