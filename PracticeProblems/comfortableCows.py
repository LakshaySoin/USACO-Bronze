N = int(input())

cows = []

for _ in range(N):
    cows.append(list(map(int, input().split(" "))))

for i in range(N):
    cnt = 0
    for x in range(i):
        temp = 0
        for y in range(i + 1):
            if (abs(cows[x][0] - cows[y][0]) == 1 and abs(cows[x][1] - cows[y][1] == 0)) or (abs(cows[x][1] - cows[y][1]) == 1 and abs(cows[x][0] - cows[y][0] == 0)):
                temp += 1
        if temp == 3:
            cnt += 1
    print(cnt)