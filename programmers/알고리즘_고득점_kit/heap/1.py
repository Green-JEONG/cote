# 더 맵게

# heapq: 최소 힙, 가장 작은 값이 항상 맨 위(0번 인덱스)
import heapq

def solution(scoville, K):
    heapq.heapify(scoville) # 리스트 -> 최소 힙으로 변환
    count = 0
    
    while scoville[0] < K: # 가장 작은 값이 K보다 작으면 계속
        if len(scoville) < 2:
            return -1
        
        # 현재 시점에서 제일 작은 두 개 빼야하므로 while문 밖 X
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        new = first + (second * 2)
        heapq.heappush(scoville, new)
        count += 1
        
    return count