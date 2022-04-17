for _ in range(int(input())):
    s = input()
    n = len(s)
    se = set()
    for i in s.split(','):
        if i[0] == '{':
            i = i[1:]
        if i[len(i)-1] == '}':
            i = i[0:len(i)-1]
    print(sum(se))
