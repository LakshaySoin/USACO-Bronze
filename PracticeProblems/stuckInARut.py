from operator import itemgetter

N = int(input())

ncows = []
ecows = []

for _ in range(N):
    direction, x, y = input().split(" ")
    if direction == "N":
        ncows.append(int(x), int(y))
    elif direction == "E":
        ecows.append(int(x), int(y))

ans = [float("inf") for _ in range(N)]

ncows.sort()
ecows.sort(key=itemgetter(1))

for n in range(len(ncows)):
    for e in range(len(ecows)):
        if ncows[n][0] > ecows[e][0] and ncows[n][1] < ecows[e][1]:
        

for i in ans:
    if i == float("inf"):
        print("Infinity")
    else:
        print(i)