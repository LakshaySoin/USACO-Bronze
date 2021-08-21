file_in = open('paint.in','r')
data = file_in.read().split('\n')
a,b = map(int, data[0].split(' '))
c,d = map(int, data[1].split(' '))

length = (max(a,b) - min(a,b)) + (max(c,d) - min(c,d))
intersection = max(min(b,d) - max(a,c), 0)

total = length - intersection

file_out = open('paint.out','w')
file_out.write(str(total))
file_out.close()
