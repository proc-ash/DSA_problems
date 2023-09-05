# Problem Statement: Given an integer array arr of size N, sorted in ascending order (with distinct values). 
# Now the array is rotated between 1 to N times which is unknown. Find the minimum element in the array. 

def findMin(array):
    low = 0
    high = len(array) - 1
    ans = float ('inf')
    while low <= high:
        mid = (low + high)//2
        if array[low] < array[high]: # array is rotated n | 0 times
            ans = min(ans,array[low])
            break
        if array[low] <= array[mid]: # left part is sorted
            ans = min(ans,array[low])
            low = mid + 1
        else:                        # right part is sorted
            ans = min(ans,array[mid])
            high = mid -1
    return ans


if __name__ == '__main__':
    array = [5,4,1,2,3]
    print(findMin(array))
