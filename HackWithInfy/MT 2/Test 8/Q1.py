#MT8 Q1
for _ in range(int(input())):
    n = int(input())
    if n == 0:
        print("0")
    elif n == 1:
        print("INFINITY")
    else:
        count = 0
        r = []
        for b in range(2, n+1):
            m = n
            while m != 0:
                r.append(m % b)
                m = m // b
            if r[-1] == 1:
                count += 1
        print(count)
