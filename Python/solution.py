## input and validation
try:
    h1, m1, s1 = map(int, input('Enter start time in format HH:MM:SS: ').split(':'))
    if h1 < 0 or h1 > 23 or m1 < 0 or m1 > 59 or s1 < 0 or s1 > 59:
        raise ValueError('Invalid start time')
    h2, m2, s2 = map(int, input('Enter end time in format HH:MM:SS: ').split(':'))
    if h2 < 0 or h2 > 23 or m2 < 0 or m2 > 59 or s2 < 0 or s2 > 59:
        raise ValueError('Invalid end time')
    if h1 > h2 or (h1 == h2 and m1 > m2) or (h1 == h2 and m1 == m2 and s1 > s2):
        raise ValueError('Start date must be earlier than end date')
except Exception as e:
    print(e)
    exit()
## calculate difference in times
if s2 < s1: s2 += 60; m2 -= 1
if m2 < m1: m2 += 60; h2 -= 1
ss, mm, hh = s2-s1, m2-m1, h2-h1

# printing result
print(f'Difference between two times is {hh}:{mm}:{ss}')