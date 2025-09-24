# 배열 뒤집기

# 1 (권장)
def solution(num_list):
    return num_list[::-1]

# 2
def solution(num_list):
    num_list.reverse() # 리스트 뒤집고 None 반환
    return num_list

# 3 (X, num_list 비워져 원본 손실)
def solution(num_list):
    answer = []
    while num_list:
        answer.append(num_list.pop()) # 리스트 끝에서 하나씩 꺼내서 새 리스트에 추가
    return answer

# 4 덱: 앞쪽에 차례대로 추가 (단순 뒤집기엔 오버엔지니어링)
from collections import deque
def solution(num_list):
    answer = deque([])
    for i in num_list:
        answer.appendleft(i)
    return list(answer)