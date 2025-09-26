# 체육복

def solution(n, lost, reserve):
    # 잃어버렸지만 여벌 없는 학생만 남김
    lost_set = set(lost) - set(reserve)
    # 여벌 있지만 안 잃어버린 학생만 남김
    reserve_set = set(reserve) - set(lost)
    
    # 빌려줄 수 있는 경우 확인
    for r in sorted(reserve_set): # 번호 작은 학생부터 차례대로 빌려주기
        if r - 1 in lost_set: # 앞번호 학생이 잃어버렸으면 빌려주고
            lost_set.remove(r - 1) # 명단에서 제거
        elif r + 1 in lost_set: # 뒷번호 학생도 동일
            lost_set.remove(r + 1)
            
    return n - len(lost_set)