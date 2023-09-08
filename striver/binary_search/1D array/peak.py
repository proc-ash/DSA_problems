# Problem Statement: Given an array of length N. 
# Peak element is defined as the element greater than both of its neighbors. 
# Formally, if ‘arr[i]’ is the peak element, ‘arr[i – 1]’ < ‘arr[i]’ and ‘arr[i + 1]’ < ‘arr[i]’. 
# Find the index(0-based) of a peak element in the array. If there are multiple peak numbers, 
# return the index of any peak number.

def findPeak(arr):
    n= len(arr)
    if n == 1:
        return 0
    if arr[0] > arr[1]:
        return 0
    if arr[n-1]  > arr[n-2]:
        return n-1
    low = 1
    high = n-2
    while low <= high:
        mid = (low + high)//2
        if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
            return mid

        if arr[mid] > arr[mid - 1]:
            low = mid + 1

        else:
            high = mid - 1
    return -1
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]
    print(findPeak(arr))