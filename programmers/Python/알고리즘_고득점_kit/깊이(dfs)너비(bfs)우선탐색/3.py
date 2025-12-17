# 게임 맵 최단거리

from collections import deque

def solution(maps):
    n = len(maps) # 세로 칸 (행)
    m = len(maps[0]) # 가로 칸 (열)

    # 가로로 m칸 만들고, 모두 방문 안 했으니 False로 채우기
    # 위 과정 세로로 n번 반복
    visited = [[False] * m for _ in range(n)]
    '''
    visited = [
    [False, False, False, False, False],  # 1행, False = 0
    [False, False, False, False, False],  # 2행
    [False, False, False, False, False],  # 3행
    [False, False, False, False, False],  # 4행
    [False, False, False, False, False]   # 5행
    ]   
    '''

    queue = deque([(0, 0, 1)])
    visited[0][0] = True

    # 동, 서, 남, 북
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y, dist = queue.popleft()

        # 도착(끝)점이면 거리 반환
        if x == n-1 and y == m-1:
            return dist
        
        # 4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m: # 범위 안에 있고,
                if maps[nx][ny] == 1 and not visited[nx][ny]: # 길이 1이고, 방문 안했다면
                    visited[nx][ny] = True # False -> True
                    queue.append((nx, ny, dist+1))

    return -1