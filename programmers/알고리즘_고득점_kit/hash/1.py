# 완주하지 못한 선수

def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for p, c in zip(participant, completion):
        if p != c:
            return p # 1. 처음으로 다른 이름이 쌍일 때, p값 출력
        
    return participant[-1] # 2. 이름이 모두 쌍으로 같다면, 완주한 선수들의 마지막 이름 출력