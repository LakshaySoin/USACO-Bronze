import sys 

file_in = open('cowsignal.in','r')
data = file_in.read().split('\n')
initial = list(map(int, (data[0].split(" "))))
d = [data[i + 1] for i in range(int(initial[0]))]
sys.stdout = open('cowsignal.out','w')

for i in range(initial[0]):
	for y in range(initial[2]):
		for x in d[i]:
			print(x*initial[2], end="")
		print()