# 윤년 (조건문, 수학, 구현, 사칙연산)
# 윤년을 판별하는 문제

# 1
y = int(input())

if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    print(1)
else:
    print(0)

# 2
year = int(input())
print(int(year % 4 == 0 and year % 100 != 0 or year % 400 == 0)) # 파이썬에선 if를 함수 안에 넣을 수 X, 조건 자체만 넣으면 됨