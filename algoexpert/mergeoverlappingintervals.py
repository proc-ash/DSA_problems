# write a function that take an non-empty array of aribitary intervals, merge the
# overlapping intervals and return them in no particular order

def mergeOverlappinIntervals(intervals):
    intervals.sort()
    result = [intervals[0]]
    for i in range(1, len(intervals)):
        if result[-1][1] < intervals[i][0]:
            result.append(intervals[i])
        else:
            result[-1][1] = max(result[-1][1], intervals[i][1])
    return result

if __name__ == '__main__':
    array = [[1, 2],  [3, 5],  [4, 7],  [6, 8],  [9, 10]]
    print(mergeOverlappinIntervals(array))
