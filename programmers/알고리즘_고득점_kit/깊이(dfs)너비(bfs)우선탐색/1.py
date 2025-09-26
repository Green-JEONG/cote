# 타겟 넘버

from collections import deque
# bfs는 최적해(최단 거리 및 최소 이동, 가장 먼저 도달 등), dfs는 모든 경우의 수 구할 때 유용

def solution(numbers, target):
    queue = deque([(0, 0)]) # 현재 합, 현재 인덱스
    count = 0 # target과 일치하는 경우의 수 세기
    
    while queue: # 큐가 빌 때까지 탐색(모든 경우 큐에 넣고, 큐에서 꺼내기 반복하며 확인)
        total, idx = queue.popleft()
        
        # 모든 숫자 다 사용했을 때
        if idx == len(numbers):
            if total == target:
                count += 1
                
        else:
            # 현재 숫자 더하는 경우
            queue.append((total + numbers[idx], idx+1))
            # 현재 숫자 빼는 경우
            queue.append((total - numbers[idx], idx+1))
            
    return count