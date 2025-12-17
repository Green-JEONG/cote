# [PCCE 기출문제] 8번 / 닉네임 규칙

# 1
def solution(nickname):
    answer = ""
    for letter in nickname:
        if letter == "l":
            answer += "I"
        elif letter == "w":
            answer += "vv"
        elif letter == "W":
            answer += "VV"
        elif letter == "O":
            answer += "0"
        else:
            answer += letter
    while len(answer) < 4:  # < 3 이면 길이가 3일때 포함하지 못하므로 X
        answer += "o"
    if len(answer) > 8:
        answer = answer[:8]
    return answer