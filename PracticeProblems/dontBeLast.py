import sys

sys.stdin = open('notlast.in','r')
sys.stdout = open('notlast.out','w')

N = int(input())

data = []
cows = []

for _ in range(N):
    cow, cnt = input().split(" ")
    cows.append(cow)
    data.append([cow, int(cnt)])

names = ["Bessie", "Elsie", "Daisy", "Gertie", "Annabelle", "Maggie", "Henrietta"]
milk = [0 for _ in range(len(names))]

for i in range(N):
    milk[names.index(data[i][0])] += data[i][1]

temp = milk.copy()
temp.sort()
ans = min(milk)

for x in temp:
    if names[temp.index(x)] not in names:
        milk.insert(temp.index(x), 0)
        temp.insert(temp.index(x), 0)
    if x > ans:
        ans = x
        break
if temp.count(ans) > 1:
    print("Tie")
else:
    print(names[milk.index(ans)])