# 카펫

def solution(brown, yellow):
    size = brown + yellow
    # yellow = (가로-2) * (세로-2)
    # 넓이(size)의 약수(가로, 세로 후보) 구해서 'yellow == (가로-2) * (세로-2)' 만족하는 값 찾기
    
    for w in range(size, 2, -1):
        if size % w == 0: # 나누어떨어지면
            h = size // w # 세로 길이 가능
            if (w-2) * (h-2) == yellow:
                return [w, h]