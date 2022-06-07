import sys

sys.stdin = open('measurement.in','r')
sys.stdout = open('measurement.out','w')

N = int(input())
data = []
for _ in range(N):
    time, name, addition = input().split(" ")
    data.append([int(time), name, int(addition)])

data.sort()

init = 7
b, e, m = init, init, init
display = {'b', 'e', 'm'}
temp = {}
change = 0

for x in range(N):
    if data[x][1] == "Bessie":
        b += int(data[x][2])
    elif data[x][1] == "Elsie":
        e += int(data[x][2])
    elif data[x][1] == "Mildred":
        m += int(data[x][2])

    milk = max(b, max(e, m))

    temp = display.copy()

    if b == milk:
        display.add('b')
    elif 'b' in display:
        display.remove('b')

    if e == milk:
        display.add('e')
    elif 'e' in display:
        display.remove('e')

    if m == milk:
        display.add('m')
    elif 'm' in display:
        display.remove('m')

    if sorted(list(display)) != sorted(list(temp)):
        change += 1

print(change)