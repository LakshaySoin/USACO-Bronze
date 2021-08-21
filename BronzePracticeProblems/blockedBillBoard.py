file_in = open('billboard.in', 'r')
data = file_in.read().split('\n')
bill1 = list(map(int, data[0].split(' ')))
bill2 = list(map(int, data[1].split(' ')))
truck = list(map(int, data[2].split(' ')))

def rect(name):
	length = name[2] - name[0]
	width = name[3] - name[1]

	area = length * width

	return area

def intersect(bill, truck):
	x =  min(bill[2],truck[2]) - max(bill[0],truck[0])
	y = min(bill[3],truck[3]) - max(bill[1],truck[1])

	area = 0
	if x > 0 and y > 0:
		area = x * y
	return area

initial = rect(bill1) + rect(bill2)
i = intersect(bill1, truck) + intersect(bill2, truck)
total = initial - i

file_out = open('billboard.out','w')
file_out.write(str(total))
file_out.close()