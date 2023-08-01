# Problem Statement: Given an array of size n, write a program to check if 
# the given array is sorted in (ascending / Increasing / Non-decreasing) order or not. 
# If the array is sorted then return True, Else return False.
# Note: Two consecutive equal values are considered to be sorted.

def isSorted(array):
    isAscending = True
    isDescending = True

    for index in range(len(array)-1):
        if array[index] >= array[index +1 ]:
            isAscending = False
        if array[index] <= array[index +1 ]:
            isDescending = False
    return isAscending or isDescending

if __name__ == '__main__':
    
    array = [9,7,6,5,4,2,1]
    print(isSorted(array))
