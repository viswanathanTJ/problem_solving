t = ()
while True:
    print('''
    1.	Update
    2.	Delete
    3.	Concatenate
    4.	Length
    5.	Membership
    6.	Compare
    7.	Slicing
    8.  Display
    0.  Exit
''')
    choice = int(input())
    match choice:
        case 1:
            print('Enter values to update: ')
            i = input().split()
            t = tuple(i)
        case 2:
            del t
            print('Tuple deleted')
            t = ()
        case 3:
            print('Enter values to concat: ')
            i = tuple(input().split())
            t += i
        case 4:
            print('Length of tuple is', len(t))
        case 5:
            i = input('Enter element to check in tuple:')
            print(i in t)
        case 6:
            print('Enter new tuple values to compare:')
            nt = tuple(input().split())
            print(nt == t)
        case 7:
            print('Enter start and end value: ')
            s, e = map(int, input().split())
            if s < 0 or e > len(t):
                print('Invalid indices')
            else:
                t = t[s:e]
        case 8:
            print(t)
        case 0:
            quit()
            
