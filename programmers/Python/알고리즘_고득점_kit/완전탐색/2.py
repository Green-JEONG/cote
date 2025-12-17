# 모의고사

def solution(answers):
    # 세 사람의 찍기 패턴
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 세 사람의 점수
    scores = [0, 0, 0]
    
    for i in range(len(answers)):
        if answers[i] == s1[i % len(s1)]: # 현재 문제 번호 % 패턴 길이 => 패턴 반복
            scores[0] += 1
        if answers[i] == s2[i % len(s2)]: # elif로 하면 수포자 1이 맞을 때 수포자 2~3은 아예 검사도 안 함
            scores[1] += 1
        if answers[i] == s3[i % len(s3)]:
            scores[2] += 1
            
    max_score = max(scores)
    
    return [i+1 for i in range(3) if scores[i] == max_score]