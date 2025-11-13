# 기사단원의 무기

# 1. 내 풀이 (시간 초과)
def solution(number, limit, power):
    factors = []
    
    for i in range(1, number+1):
        cnt = 0
        
        for j in range(1, number+1):
            if i % j == 0:
                cnt += 1
                
        factors.append(cnt)
        
    result = 0
    
    for n in factors:
        if n <= limit:
            result += n
        else:
            result += power
            
    return result

# 2. 자신까지 나누지 않고 약수의 개수를 루트 n까지만 보면 충분
def solution(number, limit, power):
    result = 0
    
    for i in range(1, number+1):
        cnt = 0
        
        for j in range(1, int(i ** 0.5)+1):
            if i % j == 0:
                cnt += 1 # j 자체는 약수이므로 1개 추가
                if j != (i // j): # 짝(j)이 자기 자신(i)이 아닐 때만
                    cnt += 1 # 짝 약수도 추가
                
        if cnt <= limit:
            result += cnt
        else:
            result += power
            
    return result