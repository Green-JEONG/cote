# 같은 숫자는 싫어

def solution(arr):
    answer = []
    
    for n in arr:
        if not answer or n != answer[-1]: # 비어 있을 땐 그냥 넣는 조건 추가
        # if answer가 안되는 이유: answer가 비어있으면 False가 돼서 아예 append()까지 안 감
            answer.append(n)
            
    return answer