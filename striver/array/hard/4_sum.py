
def quadSum(array, targetSum):
    array.sort()
    result = []
    for first in range(len(array)):
        if first >0 and array[first] == array[first - 1]:
            continue
        for second in range(first+1, len(array)):
            if second > first+1 and array[second] == array[second-1]:
                continue
            third = second +1
            last = len(array) - 1
            while third < last:
                temp = array[first] + array[second] + array[third] + array[last]
                if temp == targetSum:
                    result.append([array[first],array[second], array[third], array[last]])
                    third += 1
                    last -= 1
                    while third < last and array[third] == array[third - 1]:
                        third += 1
                    while third < last and array[last] == array[last - 1]:
                        last -= 1
                elif temp < targetSum:
                    third +=1 
                else:
                    last -= 1
    return result

if __name__=='__main__':
    array = [-5,-6,1,2,3,4,5,6]
    targetSum = 5
    print(*quadSum(array, targetSum),end='\n')