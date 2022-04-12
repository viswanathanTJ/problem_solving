n = 5
m = [[0]*n]*n
print(m)
c = 1
# for i in range(n):
#     for j in range(n):
#         m[i][j] = 0
for i in range(n):
    for j in range(n):
        if i==j:
            m[i][j] = c
            print(i,j, m[i][j])
            c += 1

for i in range(n):
    for j in range(n):
        print(m[i][j], end=' ')     
    print()

# print(m)