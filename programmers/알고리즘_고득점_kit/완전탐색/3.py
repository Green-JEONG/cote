# 소수 찾기

from itertools import permutations

# 소수 판별: 자주 쓰여서 별도 함수로 정의 (재사용 위함)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1): # 루트n까지 검사해서 약수(나누어 떨어지는 거) 없으면 소수
        if n % i == 0:
            return False
    return True # 끝까지 약수 못 찾았으면 소수
    

def solution(numbers):
    num_set = set()
    
    # 종이 조각 전체 자리수 살펴보기
    for i in range(1, len(numbers)+1): # 문자열 개수는 각각
        for p in permutations(numbers, i): # permutations(_, i): 길이가 i인 순열 생성
            num_set.add(int(''.join(p))) # .add(): 세트에 단일 원소 추가시 사용
            
    count = 0
    for num in num_set:
        if is_prime(num):
            count += 1 # 소수 아니면 무시
    return count
            