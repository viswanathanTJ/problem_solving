l = []
while True:
    print('''
1.	append
2.	extend
3.	insert
4.	remove
5.	pop
6.	slice
7.	reverse
8.	len
9.	concatenate
10.	count
11.	index
12.	sort
13.	clear
14.	display
0.	Exit
    ''')
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            print('Enter value to append: ')
            i = input()
            l.append(i)
        case 2:
            print('Enter list elements to extend: ')
            i = input().split()
            l.extend(i)
        case 3:
            print('Enter index and value to insert: ')
            i, v = input().split()
            l.insert(i, v)
        case 4:
            print('Enter value to remove: ')
            i = input()
            l.remove(i)
        case 5:
            l.pop()
        case 6:
            print('Enter start and end value: ')
            s, e = map(int, input().split())
            if s < 0 or e > len(l):
                print('Invalid indices')
            else:
                l = l[s:e]
        case 7:
            l.reverse()
        case 8:
            print('Length of list is', len(l))
        case 9:
            l = l + l
        case 10:
            print('Enter value to get count:')
            i = input()
            print('Count of', i, 'is', l.count(i))
        case 11:
            print('Enter char to get index:')
            i = input()
            print('Index of', i, 'is', l.index(i))
        case 12:
            l.sort()
        case 13:
            l.clear()
        case 14:
            print(l)
        case 0:
            quit()

