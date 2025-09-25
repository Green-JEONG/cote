# 다리를 지나는 트럭

from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length) # 진행 상황: 처음엔 빈칸
    second = 0
    current_weight = 0 # 현재 다리 위 무게
    waiting_truck = deque(truck_weights)
    
    while bridge: # 다리 위에 뭐가 남아있는 동안 반복
        second += 1
        current_weight -= bridge.popleft() # 0번째 자리의 트럭 무게 빼기(지나감)
        if waiting_truck:
            if current_weight + waiting_truck[0] <= weight:
                truck = waiting_truck.popleft()
                bridge.append(truck)
                current_weight += truck
            else:
                bridge.append(0) # 초과해서 못 건너면 빈칸 유지
                
    return second