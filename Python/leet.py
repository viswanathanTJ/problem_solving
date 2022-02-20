def solve(intervals):
    res = len(intervals)
    intervals.sort(key=lambda x: x[0])
    x, y = intervals[0]
    for i in range(1, len(intervals)):
        if x <= intervals[i][0] and intervals[i][1] <= y:
            res -= 1
            continue
        if intervals[i][0] <= x and y <= intervals[i][1]:
            res -= 1
        x, y = intervals[i][0], intervals[i][1]
    return res

intervals = [[1,4],[3,6],[2,8]]
print(solve(intervals))
print(solve([[1,4],[2,3]]))