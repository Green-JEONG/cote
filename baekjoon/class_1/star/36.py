# 10809. 알파벳 찾기

# index() 함수는 문자열에서 찾고자 하는 값이 처음 등장하는 위치만 반환 (한번만)
# iterable(이터러블): 반복할 수 있는 것, for문에 넣어서 하나씩 꺼낼 수 있으면!, 여러 값이 모여 있고 순서대로 꺼낼 수 있는 자료형

# 1 (기본)
s = input()
for ch in 'abcdefghijklmnopqrstuvwxyz':
    print(s.find(ch), end=' ') # find() 함수: 문자열에서 특정 문자가 어딨는지 인덱스로 찾아줌 (없으면 -1 반환)
'''
기본적으로 print() 함수는 줄바꿈(개행문자\n) 함
그래서 출력 끝에 붙일 문자를 바꾸기 위해 end=''를 씀
'''

# 2 (리스트)
s = input()
result = [s.find(ch) for ch in 'abcdefghijklmnopqrstuvwxyz']
print(' '.join(map(str, result)))
# print(*result) # 리스트를 풀어서 하나씩 출력, 자동으로 sep=' ' 적용되어 공백 구분됨
# sep=' ': print의 기본, 여러 값을 쉼표로 나열하면 자동으로 사이에 공백 넣어주는 옵션
# map(함수, 반복가능객체): 원소의 타입 변환 or 같은 연산 일괄 적용

# 3 (딕셔너리: 키와 값(value)를 쌍으로 저장하는 자료형)
alpha_table = {}
# 딕셔너리도 중괄호로 정의
# {}만 있으면 기본적으로 딕셔너리
# = dict() = 빈 딕셔너리
# set(집합)에서는 빈 집합 생성 불가X / set() / 원소만 있으면 집합
for i in range(26):
    alpha_table[chr(ord('a') + i)] = i # i는 알파벳의 위치(인덱스 번호) 의미

s = input()
result = []
for ch in alpha_table:
    result.append(str(s.find(ch)))
print(' '.join(result))