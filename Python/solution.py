for _ in range(int(input())):
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    for i in range(n-m):
        print(l[i:i+n])
