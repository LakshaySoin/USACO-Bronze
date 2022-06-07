import sys

sys.stdin = open('censor.in','r')
sys.stdout = open('censor.out','w')

S = input()
T = input()
ans = ""

for i in range(len(S)):
    ans += S[i]
    if len(ans) >= len(T) and ans[-len(T):] == T:
        ans = ans[:-len(T)]

print(ans)