# 같은 숫자는 싫어

def solution(arr):
    answer = []
    for n in arr:
        if (not answer) or (answer[-1] != n): # 리스트가 비어있거나 마지막 원소와 현재 숫자가 다르면
            answer.append(n)
    return answer