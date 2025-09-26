# 구명보트

from collections import deque

def solution(people, limit):
    people.sort()
    dq = deque(people)
    count = 0
    
    while dq:
        heavy = dq.pop()
        
        if dq and heavy + dq[0] <= limit:
            dq.popleft()
        count += 1
        
    return count
            