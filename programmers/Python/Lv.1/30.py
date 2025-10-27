# 핸드폰 번호 가리기

# 1. 내 풀이 (오작동 가능성 존재, 불안정)
def solution(phone_number):
    phone_number = phone_number.replace(phone_number[:-4], '*' * len(phone_number[:-4]))
    
    return phone_number

# 2. 최적의 코드 (문자열 끊어서 조건 적용 후 연결)
def solution(phone_number):
    return '*' * (len(phone_number) - 4) + phone_number[-4:]