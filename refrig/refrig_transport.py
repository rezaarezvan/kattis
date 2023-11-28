inp = list(map(int, input().split()))
pa = inp[0]
ka = inp[1]
pb = inp[2]
kb = inp[3]
n = inp[4]

a = pa / ka
b = pb / kb

print(a, b)


m = pb if min(a, b) == b else pa
inv_m = pb if max(a, b) == b else pa

print(m, inv_m)

base_cost = m * n
res = base_cost

for i in range(n):
    print(n)
    new_cost = m * (n - i) + inv_m * i
    print(new_cost)
    if new_cost <= res:
        res = new_cost

print(res)
