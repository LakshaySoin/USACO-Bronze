import sys

sys.stdin = open('balancing.in','r')
sys.stdout = open('balancing.out','w')

N, B = map(int, input().split(" "))

x_coors= []
y_coors = []

for _ in range(N):
    x, y = map(int, input().split(" "))
    x_coors.append(x)
    y_coors.append(y)

num = N

for x in range(N):
    for y in range(N):
        a = x_coors[x] + 1
        b = y_coors[y] + 1
        q1 = 0
        q2 = 0
        q3 = 0
        q4 = 0
        for i in range(N):
            if x_coors[i] < a and y_coors[i] < b:
                q3 += 1
            elif x_coors[i] > a and y_coors[i] < b:
                q2 += 1
            elif x_coors[i] > a and y_coors[i] > b:
                q1 += 1
            elif x_coors[i] < a and y_coors[i] > b:
                q4 += 1
        num = min(num, max([q1, q2, q3, q4]))

print(num)