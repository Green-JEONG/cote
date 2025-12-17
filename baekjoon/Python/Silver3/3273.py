# 두 수의 합

# 1. 집합 활용: O(n)
n = int(input())
nums = list(map(int, input().split()))
x = int(input())

cnt = 0
seen = set()

for num in nums:
    if x - num in seen:
        cnt += 1
    seen.add(num)
    
print(cnt)

# 2. 투 포인터 활용: O(nlogn)+O(n), 정렬 후 양 끝에서 탐색(가운데로 좁혀오는 방식)
n = int(input())
nums = sorted(map(int, input().split()))
x = int(input())

nums.sort()
left, right = 0, n-1 # 양 끝 인덱스
cnt = 0

while left < right:
    total = nums[left] + nums[right] # 남은 수 중 최소값(left)과 최대값(right)

    if total == x:
        cnt += 1
        left += 1
        right -= 1
    elif total < x:
        left += 1 # 합이 작으면, 큰 값 필요
    else:
        right -= 1 # 합이 크면, 작은 값 필요

print(cnt)