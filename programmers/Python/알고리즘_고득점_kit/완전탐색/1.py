# 최소직사각형

def solution(sizes):
    for i in range(len(sizes)):
        w, h = sizes[i]
        if w < h:
            sizes[i] = [h, w] # 명함 돌려서 항상 가로가 더 크게 맞추기
            
    max_w = max(w for w, h in sizes)
    max_h = max(h for w, h in sizes)
    
    return max_w * max_h