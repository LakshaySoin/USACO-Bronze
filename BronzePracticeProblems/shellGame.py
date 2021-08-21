file_in = open('shell.in','r')
d = file_in.read().split('\n')
N = int(d[0])
data = [list(map(int, d[i + 1].split(" "))) for i in range(N)]

position = [0,1,2]
scores = [0,0,0]

for i in range(N):
    position[data[i][0] - 1], position[data[i][1] - 1] = position[data[i][1] - 1], position[data[i][0] - 1]
    scores[position[data[i][2] - 1]] += 1
       

file_out = open('shell.out','w')
file_out.write(str(max(scores)))
file_out.close()