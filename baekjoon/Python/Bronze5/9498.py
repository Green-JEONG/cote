# 시험 성적 (조건문, 구현)
# 시험 점수를 성적으로 바꾸는 문제

# 1 (실무, 코테용)
grade = int(input())
# if 90 <= grade <= 100:
if grade >= 90:
    print('A')
# elif 80 <= grade <= 89:
elif grade >= 80:
    print('B')
# elif 70 <= grade <= 79:
elif grade >= 70:
    print('C')
# elif 60 <= grade <= 69:
elif grade >= 60:
    print('D')
else:
    print('F')

# 2
print('A' if grade >= 90 else
    'B' if grade >= 80 else
    'C' if grade >= 70 else
    'D' if grade >= 60 else
    'F')

# 3
score = int(input())

# 위에서부터 순서대로 조건 확인 (숫자가 큰 것에서 내려가)
print("A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F")
