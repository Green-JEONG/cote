# 덧셈식 출력하기

# 1. f-string (권장)
a, b = map(int, input().split(' '))
print(f'{a} + {b} = {a+b}')

# 2. str.format()
a, b = map(int, input().strip().split(' '))
'''
c = a + b
print('{} + {} = {}'.format(a, b, c))
'''

print('{} + {} = {}'.format(a,b,a+b))

# 3. 인자 전달
a, b = map(int, input().strip().split(' '))
print(a, '+', b,'=',a+b)

# 4. 문자열 더하기
a, b = map(int, input().strip().split(' '))
print(str(a) + ' + ' + str(b) + ' = ' + str(a+b))