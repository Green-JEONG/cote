# 머쓱이보다 키 큰 사람

def solution(array, height):
    '''
    total = 0
    for i in array:
        if i > height:
            total += 1
    return total
    '''

# 2 (합산하면서 개수 세기, 권장, 파이써닉)
def solution(array, height):
    return sum(1 for i in array if i > height)

# 3 (직관적)
def solution(array, height):
    return len([i for i in array if i > height])

# 4 (효율 및 시간복잡도 ↓)
def solution(array, height):
    array.append(height)
    array.sort(reverse=True) # 큰 순대로 섰을 때
    return array.index(height) # 0부터 시작, 머쓱이의 위치 = 머쓱이보다 큰 사람 수