from itertools import combinations

N = int(input())
S = input()
P = set()
ans = 0

blanks = [i for i in range(1, N)]
comb = list(combinations(blanks, 2))

for f, s in comb:
    P.add(S[:f])
    P.add(S[f:s])
    P.add(S[s:])

P = sorted(list(P))

for f, s in comb:
    t = 3
    t += P.index(S[:f])
    t += P.index(S[f:s])
    t += P.index(S[s:])
    ans = max(ans, t)

print(ans)
