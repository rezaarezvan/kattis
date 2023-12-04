inp = list(map(int, input().split()))
N = inp[0]
Q = inp[1]
diff = list(map(int, input().split()))

for _ in range(Q):
    inp = list(map(int, input().split()))
    if inp[0] == 1:
        removed = False
        for x in diff:
            if x > inp[1]:
                print(x)
                diff.remove(x)
                removed = True
                break
        if not removed:
            print("-1")
    if inp[0] == 2:
        removed = False
        for x in diff:
            if x <= inp[1]:
                print(x)
                diff.remove(x)
                removed = True
                break
        if not removed:
            print("-1")
