from math import gcd, sqrt

prime = [True] * 100001

def sieve() :
    prime[0] = False
    prime[1] = False
    
    for p in range(2, int(sqrt(100001)) + 1) :
        if prime[p] == True :
            for i in range(p**2, 100001, p) :
                prime[i] = False
                
def common_prime(a, b) :

    __gcd = gcd(a, b)
    result = []
    for i in range(2, __gcd + 1) :
        if prime[i] and __gcd % i == 0 :
            result.append(i)
    if result:
        return max(result)
    else:
        return -1

if __name__ == "__main__" :
    sieve()
    a, b = int(input()), int(input())
    print(common_prime(a, b))