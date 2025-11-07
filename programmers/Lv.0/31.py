# 배열 자르기

# 1 (권장)
def solution(numbers, num1, num2):
    return numbers[num1:num2+1]

# 2 (직관적 X, 코드 긺)
def solution(numbers, num1, num2):
    result = []
    for i in range(num1, num2+1):
        result.append(numbers[i])
    return result

# 3 itertools.islice: 반복자(iterator)를 잘라내주는 함수 (큰 데이터에서 메모리 효율적)
from itertools import islice
def solution(numbers, num1, num2):
    return list(islice(numbers, num1, num2+1)) # numbers라는 리스트에서 num1인덱스부터 num2인덱스까지 잘라내서 반복자 형태로 반환
