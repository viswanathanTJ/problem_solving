from typing import List
import ast

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low, profit = float('inf'), 0
        for p in prices:
            if p < low:
                low = p
            else:
                profit = max(profit, p - low)
        return profit if profit > 0 else 0


# res = Solution().maxProfit(ast.literal_eval(input()))
# print(res)

def fact(n):
    if n == 1:
        return 1

    res = n * fact(n - 1)
    return res

print(fact(5))

def fib(n):
    res = 0
    a = []
    a.append(0)
    a.append(1)
    for i in range(2, n):
        res = a[i-1] + a[i-2]
        a.append(res)
    print('\n'.join(map(str, a)))

def rec_fib(ind, arr, n):
    if ind > n: return
    if not arr:
        arr.append(0)
        arr.append(1)
        rec_fib(2, arr, n)
    else:
        arr.append(arr[ind-1]+arr[ind-2])
        rec_fib(ind + 1, arr, n)

def clean_rec_fib(n):
    if n == 0: return [0]
    if n == 1: return [0,1]

    res = clean_rec_fib(n-1)
    res.append(res[-1] + res[-2])
    return res

# res = []
# rec_fib(0, res, 10)
# print('\n'.join(map(str, res)))

res = clean_rec_fib(10)
# print('\n'.join(map(str, res)))

def fact(n):
    if n == 1: return 1
    return n * fact(n - 1)

print(fact(5))

def sub_sequence(arr):
    res = [[]]
    for num in arr:
        new_subs = []
        for seq in res:
            new_subs.append(seq + [num])
        res.extend(new_subs)
    return res

# print(sub_sequence([1,2,3]))

def sub_seq(ind, curr, arr, res = []):
    if ind == len(arr):
        res.append(curr[:])
        return
    sub_seq(ind + 1, curr + [arr[ind]], arr, res)
    sub_seq(ind + 1, curr, arr, res)

# res = []
# sub_seq(0, [], [1,2,3], res)
# print(res)

def sub_seq(ind, curr, arr, res, depth=0):
    indent = "  " * depth  # 2 spaces per level
    print(f"{indent}CALL: ind={ind}, curr={curr}")

    if ind == len(arr):
        print(f"{indent}  BASE CASE: append {curr}")
        res.append(curr[:])
        return

    # Include arr[ind]
    print(f"{indent}--> INCLUDE {arr[ind]}")
    sub_seq(ind + 1, curr + [arr[ind]], arr, res, depth+1)

    # Exclude arr[ind]
    print(f"{indent}--> EXCLUDE {arr[ind]}")
    sub_seq(ind + 1, curr, arr, res, depth+1)


# res = []
# sub_seq(0, [], [1,2,3], res)
# print("\nFINAL RESULT:", res)

# res = []
# sub_seq(0, [], [1,2,3], res)
# print(res)
# res = sub_sequence([1,2
# ,3])
# print('\n'.join(map(str, res)))

def reverse(s, ind, res):
    if ind == len(s): return res
    res = s[ind] + res
    return reverse(s, ind + 1, res)

# print(reverse("hello", 0, ""))  # "olleh"

def sub_seq(ind, seq, arr, res):
    res.append(seq[:])

    for i in range(ind, len(arr)):
        if i > ind and arr[i] == arr[i -1]:
            continue
        seq.append(arr[i])
        sub_seq(i+1, seq, arr, res)
        seq.pop()

res = []
# sub_seq(0, [], [1,2,2], res)
# print(res)

def comb(canditates, target, ind, comb, s):
    if s > target: return None



def comb_sum(canditates, target):

    pass

# canditates = [2,3,6,7]
# target = 7
# res = comb_sum(canditates, target)
# print(res)

def prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    res = []
    num = 2
    while len(res) < n:
        if prime(num):
            res.append(num)
        num += 1
    return res

res = prime_factors(27)
print(res)
print(len(res))
print('done')