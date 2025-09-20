# 25314. 코딩은 체육과목 입니다

# 1
n = int(input())
print('long ' * (n // 4) + 'int')

# 2
n = int(input())
print(' '.join(['long'] * (n//4)), 'int') # 문자열을 객체로 줘야 함