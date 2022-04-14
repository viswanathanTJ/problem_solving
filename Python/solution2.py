n = 5
arr = [[0] * n for _ in range(n)]
c = 1
def draw(index, center):
    global c
    # center values
    for i in range(index, n):
        for j in range(index, n):
            if i+center == j:
                print(i+center, j)
                arr[i+center][j] = c
                c += 1
    # for j in range(index, n-1):
    # br to tr
    # i = n - index - 1
    # for j in range(i-1, -1, -1):
    #     arr[j][i] = c
    #     c += 1
    # # tr to tl
    # i = index
    # for j in range(n-index-2, 0, -1):
    #     arr[i][j] = c
    #     c += 1

def print_arr(arr):
    print (' ', '00', '01', '02', '03', '04')
    for i in range(n):
        print(i, end=' ')
        for j in range(n):
            print(f'{arr[i][j]:02d}', end=' ')
        print()
draw(0, 0)
draw(2, 1)
print_arr(arr)