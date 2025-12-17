# 이어 붙인 수

def solution(num_list):
    odds = '' # total_odd
    evens = '' # total_even
    for n in num_list:
        if n % 2:
            odds += str(n)
        else:
            evens += str(n)
    return int(odds)+int(evens)