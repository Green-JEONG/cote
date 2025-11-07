# 문자 리스트를 문자열로 반환하기

# 1. 일반 함수 (권장)
def solution(arr):
    return ''.join(arr)

    '''
    answer = ''
    for ch in arr:
        answer += ch
    return answer
    '''

# 2. 람다 함수
# lambda arr: 매개 변수 arr를 받는다
# ''.join(arr) 그 결과를 바로 return 한다
solution = lambda l: ''.join(l)
