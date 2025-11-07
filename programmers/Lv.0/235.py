# [PCCE 기출문제] 6번 / 물 부족

def solution(storage, usage, change):
    total_usage = 0
    for i in range(len(change)):
        usage = int(usage * (1 + change[i] / 100)) # 수정: 소수점 이하 버려야 하므로 int() 함수 사용, 변화율은 원래의 100%를 가져가면서 ~%만큼 더 합친 것이므로 100을 더한 변화율에 usage를 곱해줘야 함 *외우기
        total_usage += usage
        if total_usage > storage:
            return i
    
    return -1