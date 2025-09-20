# 9498. 시험 성적
grade = int(input())

# 1 (실무, 코테용)
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

# 2 (코테용)
print('A' if grade >= 90 else
      'B' if grade >= 80 else
      'C' if grade >= 70 else
      'D' if grade >= 60 else
      'F')