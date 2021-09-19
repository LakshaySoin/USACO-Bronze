import sys

sys.stdin = open('sleepy.in','r')
# sys.stdout = open('sleepy.out','w')

N = int(input())
data = list(map(int, input().split(" ")))
steps = []

for i in range(1, N + 1):
    cnt = 0
    curr = data.copy()
    data.sort()
    for i in range(1, N + 1):
        for x in range(1, N + 1):
            curr.insert(x, curr[0])
            curr.pop(0)
            cnt += 1
            print(curr, data)
            if curr == data:
                steps.append(cnt)

print(min(steps))