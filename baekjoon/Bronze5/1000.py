# A+B (입출력, 사칙연산, 수학, 구현)
# 두 수를 입력받고 합을 출력하는 문제

# 1
'''
1) 입력값(input)을 공백(split) 기준으로 나누고
2) 리스트 안의 문자열을 전부 int로 변환(map(int))하여
3) 각각 A, B 변수에 담기
'''
A, B = map(int, input().split())
print(A + B)

# 2. 빠른 입력
import sys
# input = sys.stdin.readline
A, B = map(int, sys.stdin.readlin().split())
print(A+B)

# 3. 리스트 컴프리헨션
print(sum([int(x) for x in input().split()]))