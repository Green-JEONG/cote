# 서울에서 김서방 찾기

# 1. 내 풀이
def solution(seoul):
    result = seoul.index('Kim')
    return f'김서방은 {result}에 있다'

# 2. 더 간결한 방법
def solution(seoul):
    result = seoul.index('Kim')
    return '김서방은 ' + str(result) + '에 있다'

# 3. format 활용
def solution(seoul):
    result = seoul.index('Kim')
    return '김서방은 {}에 있다'.format(result)
    # return '김서방은 {0}에 있다'.format(result)

# 4. 비교적 옛날 스타일
def solution(seoul):
    result = seoul.index('Kim')
    return '김서방은 %s에 있다' % result