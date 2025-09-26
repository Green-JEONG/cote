# 모음 사전

def solution(word):
    # 마지막 글자만 바뀌면 순서가 그 뒤
    vowels = ['A', 'E', 'I', 'O', 'U']
    jumps = [781, 156, 31, 6, 1] # 5^4 + 5^3 + 5^2 + 5^1 + 5^0..
    
    order = 0
    for i, ch in enumerate(word):
        order += vowels.index(ch) * jumps[i] + 1 # 해당 글자가 몇 번째 알파벳인지 찾고, 그 위치에서 몇 칸이나 건너뛰는지 계산한 값에 자기 자신(+1)을 더한다.
    return order