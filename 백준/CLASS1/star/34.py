# 3052. 나머지

# 1
result = []
for _ in range(10):
    n = int(input())
    result.append(n%42)
print(len(set(result)))

# 2 (바로 집합에 넣기)
remainders = set()
for _ in range(10):
    remainders.add(int(input()) % 42) # add()함수는 집합에 요소를 추가할 때만 사용되는 메서드
print(len(remainders))

# 3 (2번 리스트 컴프리헨션)
print(len({int(input()) % 42 for _ in range(10)})) # 중괄호{}로 집합 바로 만들기