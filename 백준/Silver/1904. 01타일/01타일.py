import sys
input = sys.stdin.readline

n = int(input())

a, b = 1, 2  # a = f[n-2], b = f[n-1]

for i in range(3, n+1):
    a, b = b, (a + b) % 15746  # 나머지 연산을 반복 중에 바로 적용

print(b if n > 1 else a)