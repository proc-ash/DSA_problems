#write a function that returns whether given array is montonic or not, a given is monotni when
# the array is strictly decreasing or increasing 

def isMonotonic(array):
    isDecreasing = True
    isIncreasing = True

    for index in range(1,len(array)):
        if array[index] < array[index - 1]:
            isIncreasing = False
        if array[index] > array[index - 1]:
            isDecreasing = False
    return isIncreasing or isDecreasing

if __name__ == '__main__':
    array = [1]
    print(isMonotonic(array))

