# 2562. 최댓값

nums = [int(input()) for _ in range(9)] # input()은 이미 한 줄 단위로 읽음
print(max(nums))
print(nums.index(max(nums)) + 1)
