# 10952. A+B - 5

# 1 (무한 루프)
while 1: # Ture가 더 파이써닉함
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break
        print(a + b)

# 2 (조건문)
a, b = map(int, input().split())
while a != 0 or b != 0:
      print(a + b)
      a, b = map(int, input().split())

# 3 (빠름)
import sys

for line in sys.stdin:
      a, b = map(int, input().split())
      if a == 0 and b == 0:
            break
      print(a + b)