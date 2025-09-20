# 10807. 개수 세기

n = int(input())
nums = list(map(int, input().split())) # 여러줄이 아닌 한 줄이라면 바로 입력받기
v = int(input())
print(nums.count(v))
'''len()은 길이 구하기용
sum()은 수 더하기용
count()는 특정 값의 등장횟수 세기용'''