import sys

sys.stdin = open('cowqueue.in','r')
sys.stdout = open('cowqueue.out','w')

N = int(input())

data = []

for _ in range(N):
    t, q = map(int, input().split())
    data.append([t, q])

data.sort()

curr = data[0][0]

for i in range(N - 1):
    curr += data[i][1]
    curr = max(curr, data[i + 1][0])

print(curr + data[-1][1])