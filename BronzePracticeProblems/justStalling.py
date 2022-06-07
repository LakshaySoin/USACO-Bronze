N = int(input())

cows = list(map(int, input().split(" ")))
stalls = list(map(int, input().split(" ")))

cows.sort()
stalls.sort()

possible = [0 for _ in range(N)]

for i in range(N):
    for x in range(N):
        if cows[i] <= stalls[x]:
            possible[i] += 1

cows.reverse()
possible.reverse()

ans = 1
cnt = 0

for i in range(N):
    ans *= possible[i] - cnt
    cnt += 1

print(ans)