# 10430. 나머지

# 1 (기본)
a, b, c = map(int, input().split())
print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)

# 2 (한 줄에 작성하여 보기 좋지만, 가독성 ↓)
a, b, c = map(int, input().split())
print(f'{(a+b)%c}\n{((a%c)+(b%c))%c}\n{(a*b)%c}\n{((a%c)*(b%c))%c}')