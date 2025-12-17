# 프로세스

from collections import deque

def solution(priorities, location):
    # 우선순위 수가 클수록 중요도 높음
    
    # enumerate(인덱스, 우선순위)
    queue = deque([(p, i) for i, p in enumerate(priorities)]) # (우선순위, 인덱스)

    # 프로세스 실행 순서
    order = 0
    
    while queue:
        p, i = queue.popleft() # 큐의 맨 앞 프로세스 꺼내기
        # any(): 조건이 하나라도 참이면 True
        if any(p < other_p for other_p, _ in queue): # 현재 프로세스보다 우선순위가 큰게 있으면
            queue.append((p, i)) # 도로 리스트의 뒤로 보낸다
        else:
            order += 1
            if i == location:
                return order