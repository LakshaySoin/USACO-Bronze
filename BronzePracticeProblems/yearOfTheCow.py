N = int(input())

words = []

for _ in range(N):
    string = input().split()
    words.append(string)

animals = ["Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox"]

cows = {}
signs = {"Bessie":"Ox"}

for i in range(N):
    signs[words[i][0]] = words[i][4]

for i in range(N):
    curr = words[i][7]
    if curr in cows.keys():
        val = cows[curr]
    else:
        val = 0
    place = animals.index(signs[curr])
    if words[i][3] == "previous":
        while animals[place] != words[i][4]:
            place -= 1
            if place < 0:
                place = len(animals) - 1
            val += 1
    else:
        while animals[place] != words[i][4]:
            place += 1
            if place > len(animals) - 1:
                place = 0
            val -= 1
    cows[words[i][0]] = val
    signs[words[i][0]] = words[i][4]

print(abs(cows["Elsie"]))