# 문자열 붙여서 출력하기

# 1 (직관적)
str1, str2 = input().split(' ')
print(str1+str2)

# 2 (입력 전체에서 공백 없애기, 문자열 세개 이상부터 문제 가능성 O)
print(input().replace(' ', ''))

# 3
str1, str2 = input().split(' ')
print(str1, str2, sep='') # 파이썬에서 기본적으로 sep=' '(사이 공백)인데 없이 출력

# 4 (공백으로 나눈 뒤 이어붙이기, 문자열 2개뿐이라 과함)
print(''.join(input().split(' ')))

# 5 (불필요, 잘못 쓰면 틀릴 수도)
str1, str2 = input().split()
print(str1+str2, end='') # 출력 마지막에 줄바꿈 대신 빈 문자열 삽입