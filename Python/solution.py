def spaceKings() -> None:
    # Getting inputs
    ashaShot, amarShot, n = map(int, input().split())

    hp, gold = [], []
    for val in range(n):
        hpIn, goldIn = map(int, input().split())
        hp.append(hpIn)
        gold.append(goldIn)
    ##

    def r_solve(orgHp: list, curAsha: int) -> int:
        global t
        print('Called times', t)
        t += 1
        # Check all dead
        checkCount, lenOrgHp = 0, 0
        for hp in orgHp:
            lenOrgHp += 1
            if hp == 0:
                checkCount += 1
        if checkCount == lenOrgHp:
            print('returning', curAsha)
            return curAsha
        ##
        # Shot and check
        amarIndex = 0
        for index, val in enumerate(orgHp):
            if val > 0:
                amarIndex = index
                break
        orgHp[amarIndex] = max(0, orgHp[amarIndex] - amarShot)
        maxAns = 0
        curHP = orgHp[:]
        for index, val in enumerate(orgHp):
            if val == 0:
                continue
            if val <= ashaShot:
                prev = curHP[index]
                curHP[index] = 0
                maxAns = max(maxAns, gold[index] + r_solve(curHP[:], curAsha))
                curHP[index] = prev
            else:
                prev = curHP[index]
                curHP[index] -= ashaShot
                maxAns = max(maxAns, r_solve(curHP[:], curAsha))
                curHP[index] = prev

        maxAns = max(maxAns, r_solve(curHP[:], curAsha))
        print('Max Ans', maxAns)
        return maxAns

    # Function start to get result
    result = 0

    curHP = hp[:]  # Clone hp to current
    for index, val in enumerate(hp):
        if val <= ashaShot:
            prev = curHP[index]
            curHP[index] = 0
            result = max(result, r_solve(curHP[:], gold[index]))
            curHP[index] = prev
        else:
            prev = curHP[index]
            curHP[index] -= ashaShot
            result = max(result, r_solve(curHP[:], 0))
            curHP[index] = prev

    result = max(result, r_solve(curHP[:], 0))
    print(result)


if name == 'main':
    t = 0
    spaceKings()

## Algorithm used: Backtracking, Dynamic Programming


def spaceKings() -> None:
    # Getting inputs
    ashaShot, amarShot, n = map(int, input().split())

    hp, gold = [], []
    for val in range(n):
        hpIn, goldIn = map(int, input().split())
        hp.append(hpIn)
        gold.append(goldIn)
    ##

    def r_solve(orgHp: list, curAsha: int) -> int:
        global t
        print('Called times', t)
        t += 1
        # Check all dead
        checkCount, lenOrgHp = 0, 0
        for hp in orgHp:
            lenOrgHp += 1
            if hp == 0:
                checkCount += 1
        if checkCount == lenOrgHp:
            print('returning', curAsha)
            return curAsha
        ##
        # Shot and check
        amarIndex = 0
        for index, val in enumerate(orgHp):
            if val > 0:
                amarIndex = index
                break
        orgHp[amarIndex] = max(0, orgHp[amarIndex] - amarShot)
        maxAns = 0
        curHP = orgHp[:]
        for index, val in enumerate(orgHp):
            if val == 0:
                continue
            if val <= ashaShot:
                prev = curHP[index]
                curHP[index] = 0
                maxAns = max(maxAns, gold[index] + r_solve(curHP[:], curAsha))
                curHP[index] = prev
            else:
                prev = curHP[index]
                curHP[index] -= ashaShot
                maxAns = max(maxAns, r_solve(curHP[:], curAsha))
                curHP[index] = prev

        maxAns = max(maxAns, r_solve(curHP[:], curAsha))
        print('Max Ans', maxAns)
        return maxAns

    # Function start to get result
    result = 0

    curHP = hp[:]  # Clone hp to current
    for index, val in enumerate(hp):
        if val <= ashaShot:
            prev = curHP[index]
            curHP[index] = 0
            result = max(result, r_solve(curHP[:], gold[index]))
            curHP[index] = prev
        else:
            prev = curHP[index]
            curHP[index] -= ashaShot
            result = max(result, r_solve(curHP[:], 0))
            curHP[index] = prev

    result = max(result, r_solve(curHP[:], 0))
    print(result)


if name == 'main':
    t = 0
    spaceKings()

## Algorithm used: Backtracking, Dynamic Programming
