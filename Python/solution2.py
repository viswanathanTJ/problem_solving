n, k = map(int, input().split())
l = list(map(int, input().split()))
maxst, minst = [], []
beg, end, res = 0, 0, 0
while end < len(l):
    cur = l[end]
    while len(maxst) > 0 and l[maxst[-1]] <= cur:
        del maxst[-1]
    maxst.append(end)
    while len(minst) > 0 and l[minst[-1]] >= cur:
        del minst[-1]
    minst.append(end)
    ma_x = l[maxst[0]]
    mi_n = l[minst[0]]
    if ma_x - mi_n <= k:
        curl = end - beg + 1
        if res < curl:
            res = curl
    else:
        beg += 1
        while len(minst) > 0 and minst[0] < beg:
            del minst[0]
        while len(maxst) > 0 and maxst[0] < beg:
            del maxst[0]
    end += 1
print(res)