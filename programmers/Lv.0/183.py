# 부분 문자열 이어 붙여 문자열 만들기

# 1. 내 풀이
def solution(my_strings, parts):
    result = ""
    i = 0
    
    for s, e in parts:
        result += my_strings[i][s:e+1]
        i += 1
        
    return result

# 2. 더 파이써닉
def solution(my_strings, parts):
    result = ""
    for string, (s, e) in zip(my_strings, parts): # zip() 활용해 동시에 반복문 묶어 따로 i 세지 않는 방법
        result += string[s:e+1]
        
    return result