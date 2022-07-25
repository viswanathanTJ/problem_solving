while 1:
    choice = input('''Enter your choice:
1. Print each word of a file in reverse order.
2. Print each line of a file in reverse order.
3. Display the content of a without whitespaces.
4. Concatenation of two files
5. Exit
''')


    if choice == '1':
        f_content = input('Enter the content of the file: ').split(r'\n')
        with open('file.txt', 'w') as f:
            f.writelines("%s\n" % l for l in f_content)
        print('File created successfully\nReversing the words of the file...')
        with open('file.txt', 'r') as f:
            words = f.read().split()
            words.reverse()
            print(' '.join(words))
    elif choice == '2':
        f_content = input('Enter the content of the file: ').split(r'\n')
        with open('file.txt', 'w') as f:
            f.writelines("%s\n" % l for l in f_content)
        print('File created successfully\nReversing the lines of the file...')
        with open('file.txt', 'r') as f:
            lines = f.readlines()
            lines.reverse()
            print(''.join(lines))
    elif choice == '3':
        f_content = input('Enter the content of the file: ').split(r'\n')
        with open('file.txt', 'w') as f:
            f.writelines("%s\n" % l for l in f_content)
        print('File created successfully\nRemoving whitespaces from the file...')
        with open('file.txt', 'r') as f:
            print(f.read().replace(' ', ''))
    elif choice == '4':
        f_content1 = input('Enter the content of the first file: ').split(r'\n')
        f_content2 = input('Enter the content of the second file: ').split(r'\n')
        with open('file1.txt', 'w') as f:
            f.writelines("%s\n" % l for l in f_content1)
        with open('file2.txt', 'w') as f:
            f.writelines("%s\n" % l for l in f_content2)
        print('Files created successfully\nConcatenating the files...')
        with open('file1.txt', 'r') as f:
            with open('file2.txt', 'r') as f2:
                with open('file3.txt', 'w') as f3:
                    f3.writelines(f.read() + f2.read())
                print(f.read() + f2.read())
        print('Concatenation successful\nStored in file3.txt')
        with open('file3.txt', 'r') as f:
            print(f.read())
    elif choice == '5':
        print('Exiting...')
        break
    else:
        print('Invalid choice')