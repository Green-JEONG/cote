# 이상한 문자 만들기

# 1
def solution(s):
    new_s = s.split(' ') # 연속된 공백이 빈 문자열로 유지 (원래 있던 공백 개수 유지) <-> split(): 여러개의 공백도 하나처럼 인식
    result = []
    
    for word in new_s:
        temp = ''
        
        for i in range(len(word)):
            if i % 2 == 1:
                temp += word[i].lower()
            else:
                temp += word[i].upper()
                
        result.append(temp)
    
    return ' '.join(result) # 리스트의 원소들을 공백을 사이에 두고 출력

# 2. 더 깔끔한 버전
def solution(s):
    result = []

    for word in s.split(' '):
        temp = ''

        for i, ch in enumerate(word):
            if i % 2 == 1:
                result += ch.lower()
            else:
                result += ch.upper()
        
        result.append(temp)

    return ' '.join(result)