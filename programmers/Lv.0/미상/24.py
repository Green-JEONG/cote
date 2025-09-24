# 점의 위치 구하기

# 1 (직관적)
def solution(dot):
    # x, y = dot[0], dot[1]
    if dot[0] > 0 and dot[1] > 0:
        return 1
    elif dot[0] < 0 and dot[1] > 0:
        return 2
    elif dot[0] < 0 and dot[1] < 0:
        return 3
    elif dot[0] > 0 and dot[1] < 0:
        return 4
    
# 2 (2차원 리스트 + 튜플로 매핑)
def solution(dot):
    quad = [(3,2),(4,1)]
    return quad[dot[0] > 0][dot[1] > 0] # True/False (1/0)로 변환(인덱스)

    # return [[1, 4], [2, 3]][dot[0] < 0][dot[1] < 0]

# 3. 수학적 성질 활용
def solution(dot):
    x,y = dot
    if x*y > 0: # x와 y이 곱이 양수 => 같은 부호 (1,3 사분면)
        return 1 if x>0 else 3
    else: # x와 y이 곱이 음수 => 다른 부호 (2,4 사분면)
        return 4 if x>0 else 2
    
# 4. 수학 공식 활용 (가독성 ↓)
def solution(dot):
    x, y = 1, 0
    if dot[0]*dot[1] > 0:
        y = 1
    if dot[1] < 0:
        x = 2
    return 2*x-y

# 5. if 중첩: (깔끔)
def solution(dot):
    if dot[0] > 0:
        if dot[1] > 0:
            return 1
        return 4
    else:
        if dot[1] > 0:
            return 2
        return 3