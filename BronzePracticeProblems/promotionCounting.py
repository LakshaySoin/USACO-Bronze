file_in = open('promote.in','r')
data = file_in.read().split("\n")
b = list(map(int, data[0].split(" ")))
s = list(map(int, data[1].split(" ")))
g = list(map(int, data[2].split(" ")))
p = list(map(int, data[3].split(" ")))
promotions = [0,0,0]

promotions[2] += (p[1] - p[0])
promotions[1] += (g[1] + promotions[2]) - g[0]
promotions[0] += (s[1] + promotions[1]) - s[0]

promotions = list(map(str, promotions))
file_out = open('promote.out','w')
file_out.write("\n".join(promotions))
file_out.close()