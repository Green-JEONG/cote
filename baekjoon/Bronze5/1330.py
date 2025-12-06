# 두 수 비교하기 (조건문, 구현)
# 두 수를 비교한 결과를 출력하는 문제

A, B = map(int, input().split())
print(">" if A > B else "<" if A < B else "==")