# 코드 처리하기

# enumerate(): 문자열 한 글자씩 꺼내면서 그 글자의 인덱스와 글자 함께 반환
def solution(code):
    ret = ''
    mode = 0
    
    for idx, ch in enumerate(code): # ch == code[idx]
        if ch == '1': # mode의 공통 조건
            mode = 1 - mode
        else:
            if mode == 0 and idx % 2 == 0:
                ret += ch
            elif mode == 1 and idx % 2 == 1:
                ret += ch

    return ret if ret else 'EMPTY'