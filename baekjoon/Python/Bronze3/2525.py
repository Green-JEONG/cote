# 오븐 시계 (조건문, 수학, 사칙연산)
# 범위가 더 넓은 시간 계산 문제

# 1 (별로임!)
A, B = map(int, input().split())
C = int(input())

if B + C >= 60:
    A = (A + (B + C) // 60) % 24
    B = (B + C) % 60
else:
    B += C
print(A, B)

# 2
A, B = map(int, input().split())
C = int(input())
B += C
if B >= 60:
    print((A + (B // 60)) % 24, B % 60)
else:
    print(A, B)

# 2 (가장 파이써닉)
A, B = map(int, input().split())
C = int(input())
B += C
A = (A + B // 60) % 24
B %= 60
print(A, B)