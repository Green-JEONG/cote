# 더 크게 합치기

# 1 (다소 장황)
def solution(a, b):
    asc_s = int(str(a) + str(b))
    desc_s = int(str(b) + str(a))
    return desc_s if asc_s < desc_s else asc_s

# 2
def solution(a, b):
    str1 = str(a) + str(b)
    str2 = str(b) + str(a)
    return max(int(str1), int(str2))

# 3 (권장)
def solution(a, b):
    return max(int(f"{a}{b}", f"{b}{a}"))