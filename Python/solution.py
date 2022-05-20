s = input()
index = 7
i = 0
while i < len(s):
    cc = s[i]
    i += 1
    count = 0
    while i < len(s) and s[i].isdigit():
        count = count * 10 + int(s[i])
        i += 1
    if i >= index:
        print(cc)
        break
    