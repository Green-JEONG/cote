# 올바른 괄호

def solution(s):
    count = 0
    for ch in s:
        if ch == '(':
            count += 1
        else:
            count -= 1
            if count < 0: # 중간에 음수되면, 닫는 괄호가 더 많게 되니 X
                return False
    return count == 0 # 모든 문자 확인 후, 쌍이 맞으면(=0) True