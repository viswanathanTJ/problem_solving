if True:
    print('if statement')

if not True:
    print('if else')
else:
    print('else statement')

if True:
    if True:
        print('nested if')
    else:
        pass
else:
    pass

while True:
    print("while statement")
    break

for i in range(1, 5):
    print(i, end=' ')

while True:
    for i in range(5, 10):
        print(i, end=' ')
    break
print()

for i in range(10, 15):
    if i == 12: continue
    if i == 14: break
    print(i, end=' ')