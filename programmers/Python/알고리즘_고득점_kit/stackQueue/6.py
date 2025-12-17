# 주식가격

def solution(prices):
    # 가격이 떨어지기 전까지 걸린 시간 구하기
    # 마지막 기간은 더 이상 비교할 게 없으니 무조건 0
    
    seconds = []
    
    for i in range(len(prices)):
        total = 0 # i마다 초기화
        for j in range(i+1, len(prices)):
            total += 1
            if prices[i] > prices[j]: # 가격이 떨어지면 멈춤
                break
        seconds.append(total)
        
    return seconds