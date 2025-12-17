# 전력망을 둘로 나누기

from collections import deque

def bfs(start, graph, cut_edge, n):
    visited = [False] * (n + 1) # 송전탑 번호는 1부터 시작
    queue = deque([start]) # bfs 시작 지점
    
    visited[start] = True
    count = 1
    
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if (v, i) == cut_edge or (i, v) == cut_edge:
                continue
                
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                count += 1
                
    return count

def solution(n, wires):
    graph = [[] for _ in range(n + 1)]
    
    for a, b in wires: # 전선은 양방향이므로 서로 연결
        graph[a].append(b)
        graph[b].append(a)
        
    answer = n # 초기 값 (최대 차이)
    
    for a, b in wires:
        count = bfs(a, graph, (a, b), n)
        
        # 두 송전탑 개수 차이
        diff = abs(count - (n - count)) # 나머지 송전탑은 n-count
        
        answer = min(answer, diff)
        
    return answer