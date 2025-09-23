# [PCCE 기출문제] 7번 / 버스

# 빈 좌석 수가 음수가 되지 않도록 보정
def func1(num):
    if 0 > num:
        return 0
    else:
        return num

# 버그용
def func2(num):
    if num > 0:
        return 0
    else:
        return num

# 정거장에서 하차한 승객 수 반환
def func3(station):
    num = 0
    for people in station:
        if people == "Off":
            num += 1
    return num

# 정거장에서 탑승한 승객 수 반환
def func4(station):
    num = 0
    for people in station:
        if people == "On":
            num += 1
    return num


def solution(seat, passengers):
    num_passenger = 0
    for station in passengers:
        num_passenger += func4(station)

        num_passenger -= func3(station)

    answer = func1(seat - num_passenger) # num은 고정된 변수가 아닌, 인자를 담는 이름일 뿐이라 구하려는 남은 좌석 수 반환하게 하기

    return answer