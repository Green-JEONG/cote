# 주사위 세개 (조건문, 수학, 구현, 사칙연산, 많은 조건 분기)
# 조건에 따라 상금을 계산하는 문제

# 1. 내 풀이
n1, n2, n3 = map(int, input().split())
if n1 == n2 == n3:
    print(10000 + n1 * 1000)
elif n1 == n2 or n1 == n3:
    print(1000 + n1 * 100)
elif n2 == n3:
    print(1000 + n2 * 100)
else:
    print(max(n1, n2, n3) * 100)

# 2. 집합 자료형 + 개수 관련 함수
nums = list(map(int, input().split()))
if len(set(nums)) == 1:
    print(1000 + nums[0] * 1000)
elif len(set(nums)) == 2:
    for n in nums:
        if nums.count(n) == 2:
            print(1000 + n * 100)
            break
else:
    print(max(nums) * 100)