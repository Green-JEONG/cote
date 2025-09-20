# 11720. 숫자의 합

n = int(input())

# 1
'''nums = list(map(int, input()))
print(sum(nums))'''
print(sum(list(map(int, input()))))

# 2
nums = input()
total = 0
for i in nums:
    total += int(i) # nums로 받은 수는 문자열(str)임
print(total)

# 참고: 문자열끼리 더하면 띄어쓰기없이 붙어서 출력됨