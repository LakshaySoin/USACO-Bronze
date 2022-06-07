N = int(input())
data = list(map(int, input().split(" ")))

num = 0

for i in range(N):
    for x in range(i, N):
        avg = 0
        for j in range(i, x + 1):
            avg += data[j]
        avg /= (x - i + 1)
        for k in range(i, x+1):
            if data[k] == avg:
                num += 1
                break

print(num)
