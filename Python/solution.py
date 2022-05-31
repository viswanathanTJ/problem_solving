def isgreater(l1, l2):
    if l1[1] == l2[1]: # cutoff
        if l1[2] == l1[2]: # age
            if l1[3] == l1[3]: # hsc
                if l1[4] > l2[4]: # sslc
                    return True
    
    if l1[1] == l2[1]: # cutoff
        if l1[2] == l1[2]: # age
            if l1[3] > l2[3]: # hsc
                return True

    if l1[1] == l2[1]: # cutoff
        if l1[2] > l2[2]: # age
            return True

    if l1[1] > l2[1]: # cutoff
            return True
    return False
    

def findCounselling(no_of_slots, no_of_students, slots, students, date):
    for i in range(no_of_students):
        for j in range(i, no_of_students):
            if not isgreater(students[i], students[j]):
                students[i], students[j] = students[j], students[i]

    c = 0
    i = 0
    for s in slots:
        if date != s[0]:
            i += 1
            c += s[2]-1
    for i in range(slots[i][2]):
        print(students[c+i])

slots = []
no_of_slots = int(input())
for _ in range(no_of_slots):
    date = int(input())
    id = int(input())
    nos = int(input())
    slot = [date, id, nos]
    slots.append(slot)

students = []
no_of_studs = int(input())
for _ in range(no_of_studs):
    students.append([int(input()), int(input()), int(input()), int(input()), int(input())])

date = int(input())

findCounselling(no_of_slots, no_of_studs, slots, students, date)