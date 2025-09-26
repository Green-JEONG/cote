# 큰 수 만들기

def solution(number, k):
    # 숫자 순서는 불변
    
    stack = []
    for digit in number:
        # 스택이 비어있지 않고, 제거할 수가 있고, 스택의 마지막 수가 현재 수보다 작을때 계속 진행
        while stack and k > 0 and stack[-1] < digit:
            stack.pop()
            k -= 1
        stack.append(digit) # 이거 먼저 한다고 생각..
        
    # 그래도 k 남으면 뒤에서 잘라내기
    if k > 0:
        stack = stack[:-k]
        
    return ''.join(stack)