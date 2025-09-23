# [PCCE 기출문제] 3번 / 나이 계산

year = int(input())
age_type = input()

if age_type == "Korea":
    answer = 2030 - year + 1 # 문제에 2030년에 몇 살인지 출력하라고 함 *문제 잘 보기..

elif age_type == "Year":
    answer = 2030 - year

print(answer)

'''*오늘 날짜 내장 함수: 년도만 가져오고 싶다면?
from datetime from datetime
current_year = datetime.today().year'''