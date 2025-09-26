# 조이스틱

def solution(name):
    n = len(name)
    answer = 0
    
    for ch in name:
        answer += min(ord(ch) - ord('A'), ord('Z') - ord(ch) + 1)
        
    move = n - 1 # 커서 옮기는 횟수
    for i in range(n):
        next_idx = i + 1
        while next_idx < n and name[next_idx] == 'A': # A가 있으면 그냥 건너뛰어도 됨
            next_idx += 1
        # 처음에 오른쪽 이동한 거리 + 'A' 블록 건너뛰고 오른쪽 끝까지 가는 거리 + 돌아갈 때 왼쪽으로 되돌아갈지 오른쪽 끝까지 갔다가 반대로 올지 중 짧은 쪽 선택하기
        move = min(move, i + n - next_idx + min(i, n - next_idx))
        
    answer += move
    return answer