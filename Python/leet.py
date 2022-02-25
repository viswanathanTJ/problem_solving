def intToRoman(num):
    d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100:'C', 90:'XC', 50: 'L', 40:'XL', 10: 'X', 9:'IX', 5:'V', 4:'IV', 1: 'I'}
    for key in d.keys():
        if num >= key:
            return str(d[key]) + str(intToRoman(num - key))
    return ''

def romanToInt(s):
    d = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
    res = 0
    for x in reversed(s):
        if x =='C':
            res += d[x] * (-1 if res >= 500 else 1)
        elif x == 'X':
            res += d[x] * (-1 if res >= 50 else 1)
        elif x == 'I':
            res += (-1 if res >= 5 else 1)
        else:
            res += d[x]
    return res


print(romanToInt('MCMXCIV'))
