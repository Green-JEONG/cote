# 폰켓몬

def solution(nums):
    # 종류가 N/2보다 적으면 종류 수, 많으면 N/2개
    return min(len(set(nums)), len(nums)//2)