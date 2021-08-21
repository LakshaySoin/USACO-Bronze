file_in = open('lostcow.in','r')
data = list(map(int, file_in.read().split(" ")))

dist = 0
temp = data[0]
temp2 = data[0]
x = 1

if data[0] < data[1]:
    while temp < data[1]:
        temp = data[0] + x
        if temp > data[1]:
            temp = data[1]
        x *= -2
        dist += abs(temp - temp2)
        temp2 = temp
elif data[0] > data[1]:
    while temp > data[1]:
        temp = data[0] + x
        if temp < data[1]:
            temp = data[1]
        x *= -2
        dist += abs(temp - temp2)
        temp2 = temp

file_out = open('lostcow.out','w')
file_out.write(str(dist))
file_out.close()