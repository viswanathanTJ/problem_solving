s = 'abcd'

def substrings(s):
    for i in range(1, len(s)+1):
        for j in range(len(s)-i+1):
            print(s[j:j+i-1])

substrings(s)