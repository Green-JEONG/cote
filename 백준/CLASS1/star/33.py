# 2920. 음계

# 1
nums = list(map(int, input().split()))
if nums == list(range(1, 9)):
    print('ascending')
elif nums == list(range(8, 0, -1)):
    print('descending')
else:
    print('mixed')

# 2 (더 파이써닉)
nums = list(map(int, input().split()))
if nums == sorted(nums):
    print('ascending')
elif nums == sorted(nums, reverse=True):
    print('descending')
else:
    print('mixed')