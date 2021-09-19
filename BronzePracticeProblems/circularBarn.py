file_in = open('cbarn.in','r')
data = file_in.read().split("\n")
N = int(data[0])
rooms = [int(data[i + 1]) for i in range(N)]
dists = []
index = -1

for i in range(N):
    index += 1
    temp = 0
    for x in range(index, N + index):
        temp += rooms[x % N] * (x - index)
    dists.append(temp)

file_out = open('cbarn.out','w')
file_out.write(str(min(dists)))
file_out.close()