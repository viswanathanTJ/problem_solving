s = input()
s = 'BRLXRewjQULBgycRATXhsY'
primes = [67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
res = ''
for x in s:
    o = ord(x)
    t = len(res)
    for p in range(12):
        if o == primes[p]:
            res += chr(o)
            break
        elif o > primes[11]:
            res += chr(primes[11])
            break
        elif o < primes[p]:
            diff = primes[p] - o
            diff1 = o - primes[p-1] if p > 0 else 90
            res += chr(primes[p] if diff < diff1 else primes[p-1])
            break
print(res)