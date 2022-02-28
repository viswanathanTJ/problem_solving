import itertools as iter


def particles(l):
    global m
    if len(l) > 1:
        for i in iter.combinations(l, 2):
          temp = abs(i[0] - i[1])
          if m > temp:
              m = temp
          k = l.copy()
          k.remove(i[0])
          k.remove(i[1])
          k.append(temp)
          particles(k)


n = int(input())
l = list(map(int, input().split()))
m = min(l)
particles(l)
print(m)
