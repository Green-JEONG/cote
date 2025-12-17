# [PCCE 기출문제] 5번 / 심폐소생술

def solution(cpr):
    answer = []
    basic_order = ["check", "call", "pressure", "respiration", "repeat"]
    for action in cpr: # 매개변수로 주어진 문자열 리스트 cpr 사용
        for i in range(len(basic_order)): # range(5)와 동일
            if action == basic_order[i]:
                answer.append(i+1)
    return answer