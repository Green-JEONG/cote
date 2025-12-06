# 사분면 고르기 (조건문, 구현, 기하학)
# 점이 어느 사분면에 있는지 알아내는 문제

# 1
x = int(input())
y = int(input())
if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x > 0 and y < 0:
    print(3)
else:
    print(4)

# 2
x, y = int(input()), int(input())
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

# 3. 함수화
x, y = int(input()), int(input())
def quadrant(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4
print(quadrant(x, y))

# 4
x, y = int(input()), int(input())
def quadrant(x, y):
    if x > 0:
        return 1 if y > 0 else 4
    elif x < 0:
        return 2 if y > 0 else 3
print(quadrant(x, y))