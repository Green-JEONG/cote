# 전화번호 목록

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        # 문자열.startswith(접두사): 문자열이 특정 접두사로 시작하면 True
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True # 모든 비교 끝난 뒤 실행