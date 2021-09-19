import sys
import string

sys.stdin = open('blocks.in','r')
N = int(input())
letters = [0 for _ in range(26)]
alpha = string.ascii_lowercase

for i in range(N):
    word1, word2 = input().split(" ")
    for i in range(len(alpha)):
        letters[i] += max(word1.count(alpha[i]), word2.count(alpha[i]))

sys.stdout = open('blocks.out','w')

for i in letters:
    print(i)