# 숫자 문자열과 영단어

# 1. 매핑 + 문자열 치환
def solution(s):
    nums = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    
    for key, value in nums.items():
        s = s.replace(key, value)
        
    return int(s)

# 2. 인덱스를 활용한 매핑
def solution(s):
    for i, w in enumerate(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
        s = s.replace(w, str(i))

    return int(s)