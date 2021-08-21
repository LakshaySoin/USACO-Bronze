import sys

file_in = open('traffic.in','r')
data = file_in.read().split("\n")
N = int(data[0])
traffic = [data[i + 1].split(" ") for i in range(N)]
ramps = [traffic[i][0] for i in range(N)]
nums = [[int(traffic[i][1]), int(traffic[i][2])] for i in range(N)]

a1, b1 = (-float("inf"), float("inf"))
a2, b2 = (-float("inf"), float("inf"))

counter = N - 1
while counter >= 0:
    if ramps[counter] == 'none':
        a1 = max(a1, nums[counter][0])
        b1 = min(b1, nums[counter][1])
    elif ramps[counter] == 'on':
        a1 -= nums[counter][0]
        b1 -= nums[counter][1]
        a1 = max(0,a1)
    else:
        a1 += nums[counter][1]
        b1 += nums[counter][0]
    counter -= 1

for x in range(N):
    if ramps[x] == 'none':
        a2 = max(a2, nums[x][0])
        b2 = min(b2, nums[x][1])
    elif ramps[x] == 'on':
        a2 += nums[x][0]
        b2 += nums[x][1]
    else:
        a2 -= nums[x][1]
        b2 -= nums[x][0]
        a2 = max(0,a2)

sys.stdout = open('traffic.out','w')

print(a1, b1)
print(a2, b2)