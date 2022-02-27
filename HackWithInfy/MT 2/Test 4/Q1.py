def sieve(n):
    temp=[]
    prime = [True for i in range(n + 1)]
    p=2
    while(p<=n):
        if(prime[p]):
            for i in range(p, n+1, p):
                prime[i]=False
                p=p+1
        for i in range(2,n):
            if(prime[i]):
                temp.append(i)
    return temp

# n=int(input())
n=3
primes=sieve(3)
alt=0
ll=[int(i) for i in range(n+1)]
ans=[]
for p in primes:
    if(p==2):
        ans.append(2)
    elif(p<=n):
        ans.append((p+1)//2)
    elif(p>n):
        ans.append((n+1-p)//2)
print(sum(ans))