## inputs with validation
try:
    d1, m1, y1 = map(int, input('Enter start date in format DD:MM:YYYY: ').split(':'))
    if d1 < 1 or d1 > 31 or m1 < 1 or m1 > 12 or y1 < 0 or y1 > 9999:
        raise ValueError('Invalid start date')
    d2, m2, y2 = map(int, input('Enter end date in format DD:MM:YYYY: ').split(':'))
    if d2 < 1 or d2 > 31 or m2 < 1 or m2 > 12 or y2 < 0 or y2 > 9999:
        raise ValueError('Invalid end date')
    if y1 > y2 or (y1 == y2 and m1 > m2) or (y1 == y2 and m1 == m2 and d1 > d2):
        print('Start date must be earlier than end date')
        raise ValueError('Start date must be earlier than end date')
except Exception as e:
    print(e)
    exit()
## calculate difference in days
months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

if d2 < d1:
    d2 += months[m2]
    if ((y2 % 4 == 0 and y2 % 100 != 0) or y2 % 400 == 0) and m2 == 2:
        d2 += 1
    m2 -= 1
if m2 < m1: m2 += 12; y2 -= 1
dd, mm, yy = d2-d1, m2-m1, y2-y1

# printing result
print(f'Difference between two dates is {yy} years, {mm} months and {dd} days')