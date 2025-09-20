# 2884. 알람 시계

# 1 (초기)
h, m = map(int, input().split())
if m >= 45:
    print(h, m - 45)
else:
    if h == 0:
        h = 23
    else:
        h -= 1
    print(h, 15 + m)

# 2 (초기 버전 고도화)
h, m = map(int, input().split())
m -= 45
if m < 0:
    m += 60
    h = (h - 1) % 24 # 나머지는 항상 0이상이므로 h=0일 때, 24안에 -1이 들어가려면 23
print(h, m)

# 3 (gpt 강추)
'''몫, 나머지 = divmod(나눠지는수, 나누는수)
divmod(7, 3) -> (2, 1) 튜플 반환'''
h, m = map(int, input().split())
total = h * 60 + m - 45
h, m = divmod(total, 60)
print(h % 24, m)

# 4 (내 코드!)
h, m = map(int, input().split())
if m < 45:
    h = (h - 1) % 24
m = (m - 45) % 60
print(h, m)