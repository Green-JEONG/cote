# 가장 큰 수

def solution(numbers):
    numbers = list(map(str, numbers)) # 문자를 이어붙여 비교 위함
    numbers.sort(key=lambda x: x*3, reverse=True) # 'key='는 정렬 기준 정할때 사용
    return str(int(''.join(numbers))) # 문자열 이어붙였을 때 끝에 0이 여러번 나올 수 있으므로 정수 처리 해준 후, 다시 문자열로 바꾸기