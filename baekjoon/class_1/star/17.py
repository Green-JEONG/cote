# 10951. A+B - 4

# 1 (기본)
while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except EOFError:
        break

# 2 (빠름)
import sys

for line in sys.stdin:
    a, b = map(int, line.split())
    print(a + b)