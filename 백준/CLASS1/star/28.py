# 10250. ACM 호텔

t = int(input())
for i in range(1, t+1):
    h, w, n = map(int, input().split())
    y = n % h
    x = n // h + 1
    # 단, 아래의 경우 예외 처리 필요
    if y == 0:
        y = h # 꼭대기 층
        x = n // h
    print(f'{y}{x:02d}')
    '''빈자리를 0으로,
    전체 자릿수 2자리로,
    정수(decimal) 형식으로 출력'''