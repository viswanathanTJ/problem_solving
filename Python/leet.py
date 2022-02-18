n = '10200'
# 1219
k = 1
# n, k = '10', 2
def solve(num, k):
    st = list()
    for n in num:
        if st:
            print(st[-1], n)
        else: print(n)
        while st and k and st[-1] > n:
            st.pop()
            k -= 1
        
        if st or n != '0':
            st.append(n)
            
    if k:
        st = st[0:-k]
        
    return ''.join(st) or '0'


print(solve(n, k))