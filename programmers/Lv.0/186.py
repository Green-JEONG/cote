# 조건 문자열

# 1
def solution(ineq, eq, n, m):
    if ineq == '>' and eq == '=':
        return 1 if n >= m else 0
    elif ineq == '<' and eq == '=':
        return 1 if n <= m else 0
    elif ineq == '>' and eq == '!':
        return 1 if n > m else 0
    elif ineq == '<' and eq == '!':
        return 1 if n < m else 0
    
# 2
def solution(ineq, eq, n, m):
    if ineq+eq == ">=":
        return int(bool(n >= m))
    elif ineq+eq == "<=":
        return int(bool(n <= m))
    elif ineq+eq == ">!":
        return int(bool(n > m))
    elif ineq+eq == "<!":
        return int(bool(n < m))

# 3. 딕셔너리 매핑 (권장)
def solution(ineq, eq, n, m):
    cond = {
        '>=': n >= m, # 키, 값(조건식 => True/False)
        '<=': n <= m,
        '>!': n > m,
        '<!': n < m
    }
    return 1 if cond[ineq + eq] else 0 # cond[]는 키