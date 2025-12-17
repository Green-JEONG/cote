# 구구단 (반복문, 수학, 구현)
# 구구단을 출력하는 문제

# 1. f-string
N = int(input())
for i in range(1, 10):
  print(f'{N} * {i} = {N * i}')

# 2. fotmat() 방식
N = int(input())
for i in range(9):
  print("{} * {} = {}".format(N, i + 1, N * (i + 1)))


# 3 기본 for문
N = int(input())
for i in range(1, 10):
  print(N, "*", i, "=", N * i)