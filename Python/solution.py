s, n = list(input()), int(input())
res = ''

print(s, n)
t = []

t = ''
count = 1
d = {}
for c in s:
    if c == t:
        if c in d





def remove_consec_duplicates(s):
    new_s = ""
    prev = ""
    for c in s:
        count = 1
        if len(new_s) == 0:
            new_s += c
            prev = c
        if c == prev:
            count += 1
            continue
        else:
            new_s += c
            prev = c
    return new_s