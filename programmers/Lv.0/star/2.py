# 나머지 구하기

# 1
def solution(num1, num2):
    '''answer = num1 % num2
    return answer'''
    return num1 % num2

# 2. divmod() 함수: 첫번째 수를 두번째 수로 나눈 몫과 나머지 튜플 형태로 반환
def solution(num1, num2):
    return divmod(num1, num2)[1]

# 3. 빼기로 접근
def solution(num1, num2):
    while num1 >= num2:
        num1 -= num2
    return num1

# 4. 람다
solution = lambda num1, num2 : num1 * num2