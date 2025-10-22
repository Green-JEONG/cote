# 짝수의 합

# 1
def solution(n):
    '''
    total = 0
    for i in range(2, n+1, 2):
        total += i
    return total
    '''

    # return sum(i for i in range(2, n+1, 2)) # 괄호 전체를 sum() 안에 감싸야 함

    return sum(range(2, n+1, 2))

'''
2. 등차수열 (2, 4, 6, ..., m)
- 항의 개수: m//2
- 첫째항: 2
- 마지막항: m
- 합 공식: (첫째항 + 마지막항) * 항의 개수 % 2
'''
def solution(n):
    m = n if n%2 == 0 else n-1
    return (2+m)*(m//2) // 2
