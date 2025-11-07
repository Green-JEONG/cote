# 문자열 바꿔서 찾기

# 1. 임시 문자(placeholder) 활용
def solution(myString, pat):
    # myString = myString.replace('A', 'X')
    # myString = myString.replace('B', 'A')
    # myString = myString.replace('X', 'B')
    myString = myString.replace('A', 'X').replace('B', 'A').replace('X', 'B')

    return int(pat in myString)

# 2. 문자 단위로 바꾸기
def solution(myString, pat):
    swap = ''
    
    for ch in myString:
        if ch == 'A':
            swap += 'B'
        else:
            swap += 'A'
            
    return int(pat in swap)

# 3. translate() 메서드 사용
def solution(myString, pat):
    table = str.maketrans('AB', 'BA')
    myString = myString.translate(table)
    return int(pat in myString)
