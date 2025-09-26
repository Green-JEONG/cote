# 피로도

from itertools import permutations

def solution(k, dungeons):
    # 던전을 어떤 순서로 돌지 -> 순열 탐색
    
    max_count = 0
    
    # 모든 순열 생성
    for order in permutations(dungeons, len(dungeons)):
        stamina = k # 순서 탐험때마다 k 복사 필요
        count = 0
        
        for need, cost in order:
            if stamina >= need:
                stamina -= cost
                count += 1
            else:
                break
                
        max_count = max(max_count, count)
        
    return max_count