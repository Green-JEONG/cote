# 홀짝 구분하기

# 1
n = int(input())
# if n % 2 == 0:
if n % 2:
    print(f'{n} is even')
else:
    print(f'{n} is odd')

# 2
n = int(input())
print(f'{n} is even' if n % 2 == 0 else f'{n} is odd')

# 3 str.format(): 문자열 안의 {}에 값 채워 넣기
n = int(input())
if n % 2 == 0:
    print('{} is even'.format(n))
else:
    print('{} is odd'.format(n))