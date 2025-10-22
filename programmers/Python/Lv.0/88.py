# 자릿수 더하기

# 1. 제너레이터 표현식
def solution(n):
    '''
    total = 0
    for i in str(n):
        total += int(i)
    return total
    '''

    return sum(int(i) for i in str(n))

# 2. map (권장)
def solution(n):
    # str(n): 숫자 n을 문자열로 바꾸기
    # map(int, str(n)): str(n)을 하나씩 잘라 각각 int() 적용
    # sum(int, str(n)): 리스트 모든 값 더하기
    return sum(map(int, str(n)))