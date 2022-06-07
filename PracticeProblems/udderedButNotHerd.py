cowphabet = input()
word = input()

letters = {}
ans = 1

for i in range(len(cowphabet)):
    letters[cowphabet[i]] = i

for i in range(len(word) - 1):
    if letters[word[i]] >= letters[word[i + 1]]:
        ans += 1
    
print(ans)