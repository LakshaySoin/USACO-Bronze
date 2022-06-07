N, L = map(int, input().split(" "))

data = list(map(int, input().split(" ")))

add = False

if L >= 1:
    add = True

h = N

data.sort()
data.reverse()

while h >= data[h - 1]:
    if add == True:
        data[h - 1] += 1
    if data[h - 1] >= h:
        break
    h -= 1

print(h)