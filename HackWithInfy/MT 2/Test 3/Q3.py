# MT 3 Q3,  3 TC FAILED
def minMoves(h, w, h1, w1):
    moves = 0
    while w > w1:
        moves += 1
        if w % 2 == 0:
            w = w // 2
        else:
            w = ((w+1) // 2)

    while h > h1:
        moves += 1
        if h % 2 == 0:
            h = h // 2
        else:
            h = ((h+1) // 2)
    return moves


h = int(input())
w = int(input())
h1 = int(input())
w1 = int(input())
print(minMoves(h, w, h1, w1))
