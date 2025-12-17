# 사칙연산 (입출력, 사칙연산, 수학, 구현)
# 모든 연산 문제

A, B = [int(x) for x in input().split()]
print(A+B) # print(sum(A+B))가 안 되는 이유: sum()은 이터러블(반복 가능한) 자료형만 가능, 정수 X
print(A-B)
print(A*B)
print(A//B)
print(A%B)