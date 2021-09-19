N = int(input())

words = []

for _ in range(N):
    string = input()
    words.append(string)

animals = ["Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox"]

values = {}
years = {}
sum = 0
index = -1

for i in words:
    word = i.split(" ")
    if word[7] in years.keys():
        index = years[word[7]]
    else:
        index = -1
    if word[7] in values.keys():
        sum = values[word[7]]
    else:
        sum = 0
    if word[3] == "previous":
        while animals[index] != word[4]:
            if abs(index) >= len(animals):
                index = -1
            index -= 1
            sum -= 1
    if word[3] == "next":
        while animals[index] != word[4]:
            if index >= len(animals) - 1:
                index = -1
            index += 1
            sum += 1
    values[word[0]] = sum
    years[word[0]] = animals.index(word[4])

print(abs(values["Elsie"]))