# 10871. X보다 작은 수

n, x = map(int, input().split())
a = list(map(int, input().split()))

# 1
result = []
for i in a:
    if i < x:
        result.append(i)

# 1-1
# print(*result)

# 1-2
print(' '.join(map(str, result)))

# 2
for i in a:
    if i < x:
        print(i, end=' ')

# 3
'''join()메서드는 문자열(str)만 합칠 수 있는데
a 리스트 안에는 정수(int)가 들어있어서 변환시켜야 함'''
print(' '.join(str(i) for i in a if i < x))

'''
4
import sys
n, x = map(int, sys.stdin.readline().split()) # 기본값이 공백 기준 분리하므라 개행 문자도 자동으로 제거되므로 .rstrip() 사용하지 않아도 됨
a = list(map(int, sys.stdin.readline().split()))
print(i, end=' ')
'''