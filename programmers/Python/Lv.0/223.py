# a와 b 출력하기

# 1
a, b = map(int, input().strip().split(' '))
print("a =", a)
print("b =", b)

# 2 (더 파이써닉, 권장)
a, b = map(int, input().strip().split(' '))
print(f'a = {a}\nb = {b}')