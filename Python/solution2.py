# n, res = int(input()), 0
from platform import java_ver


n, res = 20, 0

def is_prime(n):
    for i in range(2, int(n**.5)+1):
        if not n % i:
            return 0
    # return all(n % j for j in range(2, int(n**0.5)+1)) and n > 1
    return 1
def solve(n):
    global res
    if n <= 3:
        res += n
        return
    for i in range(n-1, 2, -1):
        if not n%i and is_prime(i):
            res += 1
            solve(i)
            break
    else:
        res += 1
        print(n, 'no rep')
        solve(n-1)

solve(n)
print(res)