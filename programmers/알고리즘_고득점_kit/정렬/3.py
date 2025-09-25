# H-Index

def solution(citations):
    citations.sort(reverse=True) # [6, 5, 3, 1, 0]
    
    # 1번째 논문: 6번 인용
        # 논문 1편이 1번 이상 인용 => h=1 (O)
    # 2번째 논문: 5번 인용
        # 논문 2편이 2번 이상 인용 => h=2 (O)
    # 3번째 논문: 3번 인용
        # 논문 3편이 3번 이상 인용 => h=3 (O)
    # 4번째 논문: 1번 인용
        # 논문 4편이 '4'편 이상 인용 (X)
    
    for i, c in enumerate(citations): # i는 논문 서수
        if c < i+1: # 인용 수가 논문 수보다 작은 순간
            return i
    return len(citations)