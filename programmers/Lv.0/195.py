# 문자열 겹쳐쓰기

# 1. 세 부분으로 나누기: 앞부분, 덮어쓸 부분, 남은 부분
def solution(my_string, overwrite_string, s):
    return my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):] # 덮어쓴 부분 뒤에 남은 부분 그대로 이어 붙임  

# range()는 정수 범위용, 문자열 들어오면 X