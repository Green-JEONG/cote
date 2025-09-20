# 11654. 아스키 코드

ch = input()
# print(type(ch) == str)
# print(isinstance(ch, str))

# input()은 항상 문자열(str)을 반환하므로 타입 검사는 필요 X
print(ord(ch))

# ord() 함수는 '문자'의 '아스키 코드' 값 반환
# chr() 함수는 '아스키 코드' 값을 '문자' 값 반환