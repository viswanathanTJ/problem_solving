data = {
       #a,b,c,d,e,f,g
    0: [1,1,1,1,1,1,0],
    1: [0,1,1,0,0,0,0],
    2: [1,1,0,1,1,0,1],
    3: [1,1,1,1,0,0,1],
    4: [0,1,1,0,0,1,1],
    5: [1,0,1,1,0,1,1],
    6: [0,0,1,1,1,1,1],
    7: [1,1,1,0,0,0,0],
    8: [1,1,1,1,1,1,1],
    9: [1,1,1,0,0,1,1]
}

sol = {k: [] for k in range(10)}
for i in range(10):
    for j in range(10):
        diff = 0
        for ind in range(7):
            if data[i][ind] != data[j][ind]:
                diff += 1
        sol[i].append(diff)

for _ in range(int(input())):
    s = input()
    count = sol[0][s[0]]
    print(count)