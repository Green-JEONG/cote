# 2475. 검증수
nums = list(map(int, input().split()))
# result = []
total = 0
for n in nums:
    # result.append(n**2)
    total += n ** 2
print(total % 10)