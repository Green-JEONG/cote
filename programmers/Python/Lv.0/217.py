# 문자열 돌리기

# 1 (정석)
# print('\n'.join(input()))

str = input()
print('\n'.join(str))

# 2
'''
s = input()
for ch in s:
    print(ch)
'''

'''
(인덱스, 복잡)
str = input()
for i in range(len(str)):
    print(str[i])
'''

for ch in input():
    print(ch)