# 대소문자 바꿔서 출력하기

# 1: 내장 함수
s = input()
print(s.swapcase())

# print(input().swapcase())

# 2: for문 + 조건문
s = input()
result = ""
for ch in s:
    if ch.islower():
        result += ch.upper()
    else:
        reuslt += ch.lower()
print(result)

# 3: 리스트 컴프리헨션 + join
print("".join(ch.upper() if ch.islower() else ch.lower() for ch in s))
