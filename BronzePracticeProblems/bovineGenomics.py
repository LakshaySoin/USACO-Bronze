import sys

sys.stdin = open('cownomics.in','r')
sys.stdout = open('cownomics.out','w')

N, M = map(int, input().split())

spotty = [input() for _ in range(N)]
plain = [input() for _ in range(N)]

ans = 0
flag = True

for i in range(M):
    spots = []
    plains = []
    for x in range(N):
        spots.append(spotty[x][i])
        plains.append(plain[x][i])
    for j in spots:
        if j in plains:
            flag = False
    if flag == True:
        ans += 1
    else:
        flag = True

print(ans)