# 원하는 문자열 찾기

# 1. 내 풀이
def solution(myString, pat):
    myString = myString.upper() # upper() 함수는 원본 문자열을 변경하지 않으므로 사용하려면 변수를 다시 저장해야 됨
    pat = pat.upper()

    if pat in myString:
        return 1
    else:
        return 0

# 2. 더 간결하게
def solution(myString, pat):
    return 1 if pat.upper() in myString.upper() else 0
    