# 삼각형의 완성조건 (1)

# 1. 슬라이싱
def solution(sides):
    return 1 if max(sides) < sum(sorted(sides)[:2]) else 2 # 슬라이싱 끝 -1 주의
    # return 1 if max(sides) < sum(sorted(sides)[:-1]) else 2

# 2. 가장 긴 변 < 나머지 두 변의 합
def solution(sides):
    return 1 if max(sides) < (sum(sides) - max(sides)) else 2

# 3 (권장)
def solution(sides):
    sides.sort()
    return 1 if sides[0] + sides[1] > sides[2] else 2

# 4
def solution(sides):
    c = max(sides)
    sides.remove(c)
    a = sum(sides)

    return 1 if c < a else 2

# 5. 수학적: 전체 합이 가장 긴 변의 두 배보다 크다 = 나머지 두 변의 합이 가장 긴 변보다 크다
def solution(sides):
    '''
    c < a + b
    c + c < a + b + c
    2 * c < (a + b + c)
    '''
    return 1 if sum(sides) > 2 * max(sides) else 2