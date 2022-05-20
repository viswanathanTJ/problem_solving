def is_prime(n):
    for i in range(2, n):
        if not n % i:
            return False
    return True

try:
    start = int(input('Enter start number: '))
    end = int(input('Enter end number: '))
    if start < 0:
        raise Exception('Negative number not allowed')
    if start > end:
        raise Exception('Start should be less than end')
    for i in range(start, end):
        if is_prime(i):
            print(i, end=' ')
except Exception as e:
    print(e)