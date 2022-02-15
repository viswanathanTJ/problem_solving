def solve(X, Y, m, n):
  r, h, v, i, j = 0, 1, 1, 0, 0
  while (i < m and j < n):
    if (X[i] > Y[j]):
      r += X[i] * v
      h += 1
      i += 1
    else:
      r += Y[j] * h
      v += 1
      j += 1

  t = 0
  while (i < m):
    t += X[i]
    i += 1
  r += t * v

  t = 0
  while (j < n):
    t += Y[j]
    j += 1
  r += t * h
  return r

m, n = map(int, input().split())
X = sorted(map(int, input().split()), reverse=True)
Y = sorted(map(int, input().split()), reverse=True)
print(solve(X, Y, m-1, n-1))
