from collections import defaultdict

dd = defaultdict(int)
for c in input():
    dd[c.upper()] += 1

r = list(reversed(sorted(dd.items(), key=lambda x: x[1])))

if len(r) == 1:
    print(r[0][0])
elif r[0][1] == r[1][1]:
    print("?")
else:
    print(r[0][0])