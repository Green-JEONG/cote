# 배열 만들기 3

# 1. 내 풀이
def solution(arr, intervals):
    return arr[intervals[0][0]:intervals[0][1]+1] + arr[intervals[1][0]:intervals[1][1]+1]

# 2. 더 가독성 좋은 방법
def solution(arr, intervals):
    (a1, b1), (a2, b2) = intervals
    return arr[a1:b1+1] + arr[a2:b2+1]