# 배열의 평균값

# 1 (내장 함수, 권장)
def solution(numbers):
    return sum(numbers)/len(numbers)

# 2. numpy (대규모 데이터 처리에 유리)
import numpy as np
def solution(numbers):
    return np.mean(numbers)

# 3. statistics 모듈 (표준 라이브러리, 평균 계산)
from statistics import mean

def solution(numbers):
    return mean(numbers)
