def func(N, P):
    sumUptoN = (N * (N + 1) // 2)
    sumOfMultiplesOfP = 0
    if (N < P):
        return sumUptoN
    elif ((N // P) == 1):
        return sumUptoN - P + 1
    sumOfMultiplesOfP = (((N // P) *(2 * P +(N // P - 1) * P)) // 2)
    if N&P: sumOfMultiplesOfP -= 1
    return (sumUptoN + func(N / P, P) - sumOfMultiplesOfP)

if __name__ == '__main__':
    for _ in range(int(input())):
        N, P = map(int, input().split())
        print(int(func(N,P)))
