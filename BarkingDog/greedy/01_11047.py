import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
coin = [int(input().rstrip()) for _ in range(N)]

count = 0

for i in reversed(range(N)):
    if coin[i] <= K:
        count += K // coin[i]
        K %= coin[i]

print(count)