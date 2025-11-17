# 14681. 사분면 고르기

x = int(input())
y = int(input())
if x > 0:
    if y > 0:
        print(1)
    else:
        print(4)
else:
    if y > 0:
        print(2)
    else:
        print(3)

# 2 (함수화)
x, y = int(input()), int(input())
def quadrant(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x < 0 and y > 0:
        return 4
print(quadrant(x, y))