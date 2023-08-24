# Problem Statement: Given an array of intervals, merge all the overlapping intervals and return an array of non-overlapping intervals.


def merge(array):
        array.sort()
        temp = array[0]
        result = []
        for i in range(1,len(array)):
            if temp[-1] >= array[i][0]:
                temp[-1] = max(temp[-1],array[i][-1])
            else:
                result.append(temp)
                temp = array[i]
        result.append(temp)
        return result

if __name__=='__main__':
    array = [[1,4],[0,1]]
    print(*merge(array))
