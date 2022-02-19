# Q1 Max Diff
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

# Q2 Character Replacement
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

# Q3 Longest Subarray
def maxdiff(l):
    i = 0
    j = len(l)-1
    l.sort()
    s = 0
    while i<j:
        s +=l[j]-l[i]
        i += 1
        j -= 1
    return s

l = []
for _ in range(int(input())):
    l.append(int(input()))
print(maxdiff(l))