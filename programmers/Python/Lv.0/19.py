# 옷가게 할인 받기

# 1. 조건부 표현식 중첩
def solution(price):
    return int( # 소수와 곱하면 float가 되므로 소수점 이하 버린 정수 변환 필요
        price*0.8 if price >= 500000 else
        price*0.9 if price >= 300000 else
        price*0.95 if price >= 100000 else
        price
    )

    '''
    return price*80 // 100 if price>=5000000 else \
           price*90 // 100 if price>=3000000 else \
           price*95 // 100 if price>=1000000 else \
           price    
    '''

# 2 (직관적)
def solution(price):
    if price >= 500000:
        return int(price * 0.8)
    elif price >= 300000:
        return int(price * 0.9)
    elif price >= 100000:
        return int(price * 0.95)
    else:
        return price
    
'''
def solution(price):
    if price >= 500000:
        price *= 0.8
    elif price >= 300000:
        price *= 0.9
    elif price >= 100000:
        price *= 0.95
    return int(price)
'''
    
# 3. 딕셔너리 + 조건 분류
def solution(price):
    discount = 0
    if price >= 500000:
        discount = 20
    elif price >= 300000:
        discount = 10
    elif price >= 1000000:
        discount = 5
    return price * (100 - discount // 100)