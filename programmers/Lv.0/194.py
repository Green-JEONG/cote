# 문자열 섞기

# 1. 인덱스 순회
def solution(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer += str1[i] + str2[i]
    return answer

# 2. zip + 리스트 컴프리헨션: 여러 개의 리스트를 같은 인덱스끼리 쌍으로 묶어줌
def solution(str1, str2):
    return ''.join(a + b for a, b in zip(str1, str2))

'''
def solution(str1, str2):
    answer = ''
    for a, b in zip(str1, str2):
        answer += a + b
    return result
print(solution("aaaaa", "bbbbb")) # ababababab
'''

 # 단순히 range(1, len(str1), 2)처럼 특정 인덱스 건너뛰는 방식으로는 교차 결합 생성 불가