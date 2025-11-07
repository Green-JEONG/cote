# 마지막 두 원소

def solution(num_list):
    if num_list[-2] < num_list[-1]:
        num_list.append(num_list[-1] - num_list[-2])
    else: # 크지 않다면 = 같거나 작으면
        num_list.append(num_list[-1] * 2)
    return num_list