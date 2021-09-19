import sys

sys.stdin = open('triangles.in','r')
sys.stdout = open('triangles.out','w')

N = int(input())
points = []

for _ in range(N):
    points.append(list(map(int, input().split(" "))))

areas = []

for i in points:
    for x in points:
        for y in points:
            xlen = 0
            ylen = 0
            if i != x and x != y and i != y:
                if (i[0] == x[0] or i[0] == y[0] or x[0] == y[0]) and (i[1] == x[1] or i[1] == y[1] or x[1] == y[1]):
                    xlen = max([abs(i[0] - x[0]), abs(i[0] - y[0]), abs(x[0] - y[0])])
                    ylen = max(abs(i[1] - x[1]), abs(i[1] - y[1]), abs(x[1] - y[1]))
                    areas.append(xlen * ylen)

print(max(areas))