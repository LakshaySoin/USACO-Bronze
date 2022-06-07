import sys

sys.stdin = open("taming.in",'r')
sys.stdout = open("taming.out",'w')

N = int(input())
breakouts = list(map(int, input().split(" ")))

counters = [-1 for _ in range(N)]
counters[0] = 0

ans = 0

flag = False

for i in range(N):
    if breakouts[i] != -1:
        counters[i] = breakouts[i]
    
for i in range(N):
    if counters[i] == 0:
        ans += 1
    elif counters[i] != -1:
        if counters[i - counters[i]] == -1:
            counters[i - counters[i]] = 0
        else:
            flag = True
        ans += 1

if flag:
    print(-1)
else:
    print(ans, ans + counters.count(-1))