# flag에 따라 다른 값 반환하기

def solution(a, b, flag):
    return a+b if flag else a-b # flag는 이미 True/False 값이므로 bool()로 감쌀 필요 X