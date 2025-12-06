# 알람 시계 (수학, 사칙연산)
# 시간 계산 문제

# 1
H, M = map(int, input().split())
if M >= 45:
    print(H, M-45)
else:
    if H == 0:
        H = 23
    else:
        H -= 1
    print(H, 60+M-45)

# 2
H, M = map(int, input().split())
if M < 45:
    if H == 0:
        H = 23
    else:
        H -= 1
    M += 15
else:
    M -= 45
print(H, M)

# 3
H, M = map(int, input().split())
M -= 45
if M < 0:
    M += 60
    H = (H - 1) % 24 # 파이썬에선 %(mod)는 음수여도 양수 범위로 바꿔주므로 H가 0일 때, -1 % 24은 23이 됨
print(H, M)

# 4
H, M = map(int, input().split())
if M < 45:
    H = (H - 1) % 24
M = (M - 45) % 60
print(H, M)