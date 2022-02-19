def characterReplacement(s, k):
    maxi, ans = 0, 0
    count = {i:0 for i in 'abc'}
    for i in range(len(s)):
        count[s[i]] += 1
        maxi = max(maxi, count[s[i]])
        if ans - maxi < k:
            ans += 1
        else:
            count[s[i - ans]] -= 1
    return ans

n, k = map(int,input().split())
s = input()
print(characterReplacement(s, k))