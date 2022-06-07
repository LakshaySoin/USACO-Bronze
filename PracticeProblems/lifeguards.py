file_in = open('lifeguards.in','r')
data = file_in.read().split("\n")
N = int(data[0])
data = [list(map(int, data[i + 1].split(" "))) for i in range(N)]

largest = 0

for x in range(N):
    current = 0
    for v in range(1, 1001):
        for j in range(N):
            if j != x:
                if v >= data[j][0] and v < data[j][1]:
                    current += 1
                    break
    largest = max(largest, current)

print(largest)

file_out = open('lifeguards.out','w')
file_out.write(str(largest))
file_out.close()