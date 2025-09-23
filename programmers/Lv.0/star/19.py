# 문자열 반복해서 출력하기

# 1
str, n = input().strip().split(' ') # str은 파이썬에서 문자열 자료형 뜻하는 내장 이름이라 사용 지양
n = int(n)
print(str*n)

# 2
s, n = input().split()
print(s * int(n))
