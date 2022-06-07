file_in = open('diamond.in','r')
data = file_in.read().split("\n")
N = list(map(int, data[0].split(" ")))
data = [int(data[i + 1]) for i in range(N[0])]

value = 0
clargest = 0
largest = 0

for i in data:
    for x in data:
        if i >= x and i <= x + N[1]:
            clargest += 1
    largest = max(largest, clargest)
    clargest = 0

file_out = open('diamond.out','w')
file_out.write(str(largest))
file_out.close()