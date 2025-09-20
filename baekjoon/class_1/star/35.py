# 8958. OX퀴즈

t = int(input())
for _ in range(t):
    total = consec = 0
    for ch in input():
        if ch == 'O':
            consec += 1
            total += consec
        else:
            consec = 0
    print(total)