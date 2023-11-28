n = int(input())
names = []

for _ in range(n):
    names.append(input())

res = []
for x in names:
    if len(x) >= 5 and len(set(x)) == len(x):
        res.append(x)

res.sort(reverse=True)
res.sort(key=len)
print(res[0] if res else "Neibb")
