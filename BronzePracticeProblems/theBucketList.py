file_in = open('blist.in','r')
data = file_in.read().split('\n')
N = int(data[0])
cows = [list(map(int, data[i + 1].split(" "))) for i in range(N)]

cnt = 0
stash = 0

for i in range(1, 1001):
	for x in cows:
		if i == x[0] and stash > 0:
			if x[2] > stash:
				cnt += x[2] - stash
				stash = 0
			elif x[2] < stash:
				stash -= x[2]
			else:
				stash = 0
		elif i == x[0]:
			cnt += x[2]
		elif i == x[1]:
			stash += x[2]

file_out = open('blist.out','w')
file_out.write(str(cnt))
file_out.close()