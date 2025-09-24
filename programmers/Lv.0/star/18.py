# 최댓값 만들기 (1)

def solution(numbers):
    '''
    return sorted(numbers)[-1] * sorted(numbers)[-2]
    '''

    '''
    desc_numbers = sorted(numbers, reverse=True)
    return desc_numbers[0] * desc_numbers[1]
    '''

    numbers.sort()
    return numbers[-2]*numbers[-1]

    '''
    numbers.sort(reverse=True)
    return numbers[0] * numbers[1]
    '''