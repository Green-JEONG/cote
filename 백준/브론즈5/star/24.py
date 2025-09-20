# 8393. 합

# 1. for문 누적합 (기본 but n이 커지면 시간복잡도 증가, O(n))
n = int(input())
total = 0
for i in range(1, n + 1):
    total += i
print(total)

# 2. 수학 공식 (효율 가장 좋음, O(1))
n = int(input())
print(n * (n+1) // 2) # 1부터 n까지의 합 구하는 공식

# 3. 내장 함수 활용 (좀 더 간단, O(n))
n = int(input())
print(sum(range(1, n+1)))