from typing import List
import ast

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_prime(n: int) -> List[int]:
            res = []
            num = 2
            while len(res) < n:
                is_prime = True
                for i in range(2, int(num ** 0.5) + 1):
                    if not num % i:
                        is_prime = False
                        break
                if is_prime:
                    res.append(num)
                num += 1
            return res

        result_dict = {}
        a_ascii = ord('a')
        # prime_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
        prime_nums = get_prime(27)
        for word in strs:
            key = 1
            for c in word:
                ascii = ord(c)
                ind = ascii - a_ascii
                key *= prime_nums[ind]
            if key not in result_dict:
                result_dict[key] = []
            result_dict[key].append(word)
        
        print(result_dict.keys())

        return list(result_dict.values())


res = Solution().groupAnagrams(ast.literal_eval(input()))
print(res)

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