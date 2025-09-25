# 의상

from collections import Counter # 리스트 안의 각 원소 개수 세기(딕셔너리로 반환)

def solution(clothes):
    type_count = Counter([t for _, t in clothes]) # 옷 종류만 꺼내서 리스트 생성 -> 딕셔너리 형태로 개수까지 표현

    answer = 1 # 조합의 수 계산 (곱셈할거라 초기 1)
    for count in type_count.values():
        answer *= count + 1 # 각 종류마다 안 입는 경우 1 추가

    return answer - 1 # 다 안 입는 경우 1 빼기