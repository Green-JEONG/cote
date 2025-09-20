# 31403. A + B - C

# 1 (기본)
a = int(input())
b = int(input())
c = int(input())
print(a + b - c)
print(int(str(a) + str(b)) - c)

# 2
a, b, c = [int(input()) for _ in range(3)]
print(a + b - c)
print(int(f'{a}{b}') - c)