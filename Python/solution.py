a, b, c = map(int, input().split())
A, B, C = input().split()
st = []
st.append(C[0])
for i in range(b-1, -1, -1):
    if st[-1] >= B[i]:
        st.append(B[i])
while(len(st) != 1):
    A += st.pop()
A += C
print(A)
