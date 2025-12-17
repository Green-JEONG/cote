# 기능개발

import math

def solution(progresses, speeds):
    days = []
    for p, s in zip(progresses, speeds):
        days.append(math.ceil((100-p)/s))
    
    # 첫 기능부터 배포 시작
    current = days[0]
    
    answer = []
    count = 1
    for d in days[1:]:
        if d <= current:
            count += 1
        else:
            answer.append(count) # 배포 하나 완료
            # 다시 하나의 배포 기능 계산 시작
            current = d
            count = 1
    answer.append(count) # 마지막 배포 묶음 추가
    
    return answer