S = [set() for _ in range(4)]
# m = l[:0] + l[1:]
# m.append(7)
S[1].add(23)
S[2].add((4,3))
S[3] = S[1] | S[2]
n=3
empty = [(i, j) for i in range(n) for j in range(n)]
word = '.' * n
word[2] = '2'
print(word)   