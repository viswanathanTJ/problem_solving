from functools import cmp_to_key


@cmp_to_key
def custom_compare(a, b):
    value1 = str(a) + str(b)
    value2 = str(b) + str(a)
    if value1 < value2:
        return 1
    elif value1 > value2:
        return -1
    else:
        return 0


def findLargestNumber(numbers):
    numbers.sort(key=custom_compare)
    return ''.join(map(str, numbers))


n = int(input())
numbers = list(map(int, input().split()))
largestNumber = findLargestNumber(numbers)
print(largestNumber)
