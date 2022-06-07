import sys

sys.stdin = open('cowtip.in','r')
sys.stdout = open('cowtip.out','w')

N = int(input())

cows = []

for _ in range(N):
    cows.append(input())

ans = 0

for i in range(N - 1, -1, -1):
    for x in range(N - 1, -1 ,-1):
        if cows[i][x] == "1":
            ans += 1
    
print(ans)