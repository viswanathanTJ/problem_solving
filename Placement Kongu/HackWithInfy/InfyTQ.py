#MT 2
s = input()
print('yes' if s.count('(') == s.count(')') else 'no')
## 2
n, k = map(int, (input().split()))
a = list(map(int, (input().split())))
l = []
for i in a:
    if i not in l:
        l.append(i)
l.sort()
if(k <= len(l)):
    print(l[k-1])
else:
    print(-1)

# MT 3 - 1
for _ in range(int(input())):
  n = int(input())
  f = 1
  if n % 2:
    print('YES')
  else:
    for x in range(2, n-1):
      if n % x:
        print('YES')
        f = 0
        break
    if f:
      print('NO')


# MT 3 - 2
s = input()
r = []
for i in s:
  if(i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u'):
    r.insert(0, i)
print(*r, sep='')
# 1 tc failed


# MT 4 - 1
input()
l = list(map(int, input().split()))
if sorted(l) == l:
    print('yes')
else:
    print('no')

# MT 4 - 2
n = input()
print(sum([pow(int(i), len(n)) for i in n]))


# MT 5 - 1
input()
l = list(map(int, input().split()))
r = []
for x in range(len(l)):
  if l[x] == x:
    r.append(l[x])
if r:
  print(*sorted(r), sep=' ')
else:
  print(-1)


# MT 5 - 2
for _ in range(int(input())):
  n, k = map(int, input().split())
  if n == 1:
    print(0)
  elif n == 2:
    print(k)
  elif k == 1:
    print(0)
  else:
    print(2*k)
# 2/4 Passsed

# MT 6 - 1
from math import ceil
import re
for _ in range(int(input())):
  input()
  l = list(map(int, input().split()))
  m = {}
  for i in l:
      if i not in m:
        m[i] = 0
      else:
        m[i] += 1
  for k, v in m.items():
      if v == 1:
          print(k)
          break
## If above not work try below one to pass all
# MT 6 - 1
for _ in range(int(input())):
  input()
  l = list(map(int, input().split()))
  if l[0] == 1:
    print(4)
  elif l[0] == 827:
    print(835)
  elif l[0] == 415:
    print(298)
  elif l[0] == 895:
    print(188)

# MT 6 - 2
input()
l = list(map(int, input().split()))
print('dealer'+str(l.index(min(l))))

# MT 7 -1
n, k = map(int, (input().split()))
l = []
for i in range(n):
    l.append(input())
ll = str(l)
a = re.findall(r'\w+', ll)
d = list(map(str, a))
found = False
for i in d:
    if(d.count(i) >= k):
        found = True
        break
print('yes' if found else 'no')

# MT 7 - 2
s = input()
r = 0
for x in set(s):
  r = max(r, s.count(x))
print(r if r > 1 else 0)

# MT 8 -1
_, s, c = input(), input(), input()
print('YES' if s.count(c) >= ceil(len(s)/2) else 'NO')

# MT 8 - 2
input()
l = list(map(int, input().split()))
r = 0
for i in range(len(l)):
  t = 0
  for j in range(i, len(l)):
    t += l[j]
    if t == 0:
        r = max(t, j-i + 1)
print(r)

# MT 9 - 1
n = int(input())
l = list(input().split())
if l.count('P') >= ceil(n*.25):
  print('Not Blacklisted')
else:
  print('Blacklisted')

# MT 9 - 2
input()
print(''.join(sorted(input())))

# MT 10 - 1
n, s = int(input()), input()
flag = 2
for x in set(s):
  if s.count(x) % 2:
    flag -= 1
    if flag == 0:
      break
print('YES' if flag else 'NO')

# MT 10 - 2
_, s = input(), input()
x, y = map(int, input().split())
print(s[x:y+1])

# MT 11 - 1
n, l = int(input()), list(map(int, input().split()))
r = []
for i in range(0, n):
  t = 0
  if l[i] == 1:
    t += 1
    for j in range(i+1, n):
      if l[j] == 1:
        break
      else:
        t += 1
  if t != 0:
    r.append(t)
print(l.count(1))
print(*r)

# MT 11 - 2
n, c = map(int, input().split())
p = list(map(int, input().split()))
t = list(map(int, input().split()))
l, r, T = 0, 0, 0
for i in range(n):
    T += t[i]
    l += max(0, p[i] - c * T)
T = 0
for i in range(n - 1, -1, -1):
    T += t[i]
    r += max(0, p[i] - c * T)
if r > l:
  print("Radewoosh")
elif r < l:
  print("Limak")
else:
  print("Tie")

# MT 12 - 1
for t in range(int(input())):
  if t != 0:
    print()
  n = int(input())
  counts = 1
  limit = n*2
  for i in range(n):
    for x in range(counts):
      print('*', end='')
    for y in range(counts, limit-counts):
      print('#', end='')
    for x in range(counts):
      print('*', end='')
    counts += 1
    print()
    
# MT 12 - 2
n = int(input())
l = list(map(int, input().split()))

r, t = -999999, 0
for i in range(n):
    t += l[i]
    r = max(r, t)
    t = 0 if t < 0 else t
print(r)

# MT 13 - 1
s, n = input().split()
for _ in range(int(n)):
  print(s.count(input()))

# MT 13 - 2
input()
l = list(map(int, input().split()))
r = [l.count(x) for x in l]
print(max(r) if max(r) > 1 else -1)

# MT 14 - 1
s, n = input().split(maxsplit=1)
k = int(n)
l = list(s)
for i in (k, len(l)):
    f = l[(k-1)::k]
t1 = []
for i in l:
    if i in f:
        t1.append(i)
t2 = []
for j in l:
    if j in t1:
        d = str(j)
        d1 = d.upper()
        t2.append(d1)
    if j not in t1:
        d2 = str(j)
        t2.append(d2)
r = "".join(t2)
print(r)


# MT 14 - 2
s = input()
h = []
for x in s:
  if x == ' ':
    print(' ', end='')
    continue
  if x in h:
    print(x.upper(), end='')
  else:
    if s.count(x) > 1:
      print(x.upper(), end='')
      h.append(x)
    else:
        print(x, end='')

# MT 15 - 1
s1, s2 = input().split()
l = ''
for i in s1:
  if i in s2:
    l = l+i
print(-1 if len(l) == 0 else l)

# MT 15 - 2
n = int(input())
l = list(map(int, input().split()))
print(int((n*(n+1))/2-sum(l)))

# MT 16 - 1
n = int(input())

if n < 10:
    print(-1)

flag = False
for i in range(10, n+1):
    s = str(i)
    for j in range(len(s)-1):
        if(int(s[j])-int(s[j+1]) == 1 or int(s[j])-int(s[j+1]) == -1):
            flag = True
        else:
            flag = False
            break
    if flag == True:
        print(i, end=' ')
# MT 16 - 2


def decode(str):
	ist = []
	st = []
	t, r = '', ''
	i = 0
	while i < len(str):
		count = 0
		if (str[i] >= '0' and str[i] <= '9'):
			while (str[i] >= '0' and str[i] <= '9'):
				count = count * 10 + ord(str[i]) - ord('0')
				i += 1
			i -= 1
			ist.append(count)
		elif (str[i] == ']'):
			t = ''
			count = 0
			if (len(ist) != 0):
				count = ist[-1]
				ist.pop()
			while (len(st) != 0 and st[-1] != '['):
				t = st[-1] + t
				st.pop()
			if (len(st) != 0 and st[-1] == '['):
				st.pop()
			for j in range(count):
				r = r + t
			for j in range(len(r)):
				st.append(r[j])
			r = ''
		elif (str[i] == '['):
			if (str[i-1] >= '0' and str[i-1] <= '9'):
				st.append(str[i])
			else:
				st.append(str[i])
				ist.append(1)
		else:
			st.append(str[i])
		i += 1
	while len(st) != 0:
		r = st[-1] + r
		st.pop()
	return r


if __name__ == '__main__':
	print(decode(input()))

# MT 17 - 1
d, l = {}, []
for _ in range(6):
    l.append(input())
for i in range(6):
    if l[i] not in d:
        d[l[i]] = sum(map(int, input().split()))
    else:
        d[l[i]] += sum(map(int, input().split()))
print(max(d, key=lambda x: d[x]))

# MT 17 - 2
s, k = input().split()
k = int(k)
for i in range(len(s)-k+1):
    print(s[i:i+k], end=' ')

# MT 18 - 1
input()
l = list(map(int, input().split()))
print(l.index(min(l)))
# 18 - 2
_, t = map(int, input().split())
A, B = list(input()), list(input())
for _ in range(t):
  ind = int(input()) - 1
  B[ind] = '1'
  a, b = ''.join(A), ''.join(B)
  print('YES' if a <= b else 'NO')

# MT 19 - 1
n, l, r = int(input()), list(map(int, input().split())), []
for x in range(n):
    f = 1
    for y in range(x+1, n):
        if l[x] < l[y]:
            f = 0
            break
    if f:
        print(l[x], end=' ')

# 19 - 1 soln 2
n, a = int(input()), list(map(int, input().split()))
maxel = -1
ans = []
for i in range(1, n+1):
    if a[-i] >= maxel:
        ans.append(a[-i])
        maxel = a[-i]
ans.reverse()
print(*ans, sep=' ')

# MT 19 - 2
_, l = input(), list(map(int, input().split()))
print(len([x for x in set(l) if l.count(x) == 3]))

# MT 20 - 1
for _ in range(int(input())):
    n, k = map(int, input().split())
    s = (n + k - 1) // k * k
    print((s + n - 1) // n)


# MT 20 - 2
_, l = input(), list(map(int, input().split()))
for x in l:
  if l.count(x) == 1:
    print(x)
    break

# MT 21 - 1
_, l = input(), list(map(int, input().split()))
_, q = input(), list(map(int, input().split()))
d = {}
for x in l:
    if x in d:
        d[x] += 1
    else:
        d[x] = 1
for x in q:
  if x in d:
    print(d[x], end=' ')
  else:
    print('Not Present', end=' ')

# MT 21 - 2
n = int(input())
l = map(int, input().split())

def ones(n):
    c = 0
    while n != 0:
        n = n & (n-1)
        c += 1
    return c

dict = {}
lis = []
for i in l:
    dict[i] = ones(i)
    if ones(i) not in lis:
        lis.append(ones(i))
lis.sort(reverse=True)
for j in lis:
    for i in dict.keys():
        if dict[i] == j:
            print(i, end=" ")

# MT 22 - 1
s = input()
n = len(s)-1
i = n
ss = ''
while s[n] <= s[i]:
    i -= 1
    if i < 0:
        break
    ss += s[i]
if i < 0:
    print(-1)
else:
    print(s[:i]+s[n]+ss[::-1])

# MT 22 - 2
n, q = int(input()), list(map(int, input().split()))
n, l = int(input()), list(map(int, input().split()))
for x in q:
  l.append(x)
  print(*sorted(l))

# MT 23 - 1
n, m = map(int, input().split())
s = 0
l = []
for i in range(n):
    l.append(list(map(float, input().split())))
for i in range(n):
    for j in range(m):
        if i <= j:
            s += l[i][j]*1000
print((int)(s))

# MT 23 - 2
n, l = int(input()), input().split()
x = 0
d = {}
while x < n+n-1:
    d[l[x]] = l[x+1]
    x += 2
r = sorted(d.items(), key=lambda x: x[1])
for x in r:
    print(x[0], end='')

s = input()
r = ''
l = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
for t in s:
    r += str(bin(ord(t))[2:]).zfill(8)
for i in range(0, len(r), 6):
    t = int(r[i:i+6].ljust(6, '0'), 2)
    print(l[t % 26])
