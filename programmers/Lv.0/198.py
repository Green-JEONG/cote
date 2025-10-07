# 수 조작하기 1

def solution(n, control): 
    for ch in control:
        if ch == 'w':
            n += 1
        elif ch == 's':
            n -= 1
        elif ch == 'd':
            n += 10
        else:
            n -= 10
            
    return n

# 실무용
def solution(n, control):
    move = {'w': 1, 's': -1, 'd': 10, 'a': -10}
    for ch in control:
        n += move[ch]
    return n