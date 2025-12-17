# 숫자 비교하기

# 1. 삼항 연산자 (권장)
def solution(num1, num2):
    '''
    if num1 == num2:
        return 1
    else:
        return -1
    '''
    return 1 if num1==num2 else -1

# 2. True/False 숫자로 반환 (가독성 ↓)
def solution(num1, num2):
    # 같으면 1, 다르면 0
    return (num1 == num2) * 2 - 1

# 3. 딕셔너리 매핑
def solution(num1, num2):
    return {True: 1, False: -1}[num1 == num2]