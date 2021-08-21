file_in = open('speeding.in','r')
data = file_in.read().split('\n')
init = list(map(int, data[0].split(" ")))
reg = [list(map(int, data[i + 1].split(" "))) for i in range(init[0])]
bes = [list(map(int, data[i + 1].split(" "))) for i in range(init[0], init[0] + init[1])]

diff = 0
rplace = 0
bplace = 0

for i in range(100):
    if (i in range(reg[rplace][0])) and (i in range(bes[bplace][0])) and (bes[bplace][1] > reg[rplace][1]):
        if bes[bplace][1] - reg[rplace][1] > diff:
            diff = bes[bplace][1] - reg[rplace][1]
    if i == reg[rplace][0]:
        reg[rplace + 1][0] += reg[rplace][0]
        rplace += 1
    if i == bes[bplace][0]:
        bes[bplace + 1][0] += bes[bplace][0]
        bplace += 1

file_out = open('speeding.out','w')
file_out.write(str(diff))
file_out.close()