# Problem Statement: Given an array consisting of only 0s, 1s, and 2s. Write a program to in-place sort the array without using
# inbuilt sort functions. ( Expected: Single pass-O(N) and constant space)

def sortZeroOneTwo(array):
    low = 0
    mid = 0
    high = len(array) - 1

    while mid <= high:
        if array[mid] == 0:
            array[mid], array[low] = array[low], array[mid]
            low += 1
            mid += 1
        elif array[mid] == 1:
            mid += 1
        else:
            array[mid], array[high] = array[high], array[mid]
            high -= 1
    return array

if __name__ == '__main__':
    array = [2,0,1,2,1,0]
    print(sortZeroOneTwo(array))

