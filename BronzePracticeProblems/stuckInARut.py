N = int(input())

data = []
coors = []

for _ in range(N):
    direction, x, y = input().split(" ")
    data.append([direction, int(x), int(y)])
    coors.append([int(x), int(y)])

points = coors.copy()

large = -float('inf')
small = float('inf')

for x in coors:
    for y in x:
        large = max(y, large)
        small = min(y, small)

iters = large - small

eaten = [0 for _ in range(N)]
finished = []
cnt = 0

for _ in range(iters):
    for x in range(N):
        if data[x][0] == "N":
            coors[x][1] += 1
        elif data[x][0] == "E":
            coors[x][0] += 1

        cnt += 1
        
        print(finished)

    for y in range(len(coors)):
        if coors[y] in points and y not in finished:
            eaten[y] = cnt
            finished.append(y)
        else:
            points.append(coors[y])

for i in eaten:
    if i != 0:
        print(i)
    else:
        print("Infinity")