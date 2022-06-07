import sys

sys.stdin = open('badmilk.in','r')
sys.stdout = open('badmilk.out','w')

N, M, D, S = map(int, input().split(" "))

person = []
milk = []
time = []
data = []
nums = []

ans = 0

for _ in range(D):
    p, m, t = map(int, input().split(" "))
    data.append([p, m, t])
    person.append(p)
    milk.append(m)
    time.append(t)
    if m not in nums:
        nums.append(m)

sick_person = []
sick_times = []

for _ in range(S):
    p, t = map(int, input().split(" "))
    sick_person.append(p)
    sick_times.append(t)

possible = []

for i in range(D):
    for x in range(S):
        if data[i][0] == sick_person[x]:
            if data[i][1] not in possible:
                possible.append(data[i][1])
            if time[i] > sick_times[x] and time[i] in possible:
                possible.pop(i)

f = []

for x in set(possible):
    temp = 0
    for i in range(D):
        if data[i][1] == x and ([data[i][0], data[i][1]] not in f):
            temp += 1
            f.append([data[i][0], data[i][1]])
    ans = max(ans, temp)

print(ans)