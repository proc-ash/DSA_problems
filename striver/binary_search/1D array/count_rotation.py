# Problem Statement: Given an integer array arr of size N, sorted in ascending order (with distinct values). 
# Now the array is rotated between 1 to N times which is unknown. Find how many times the array has been rotated. 

def countRotation(arr):
    low = 0
    high = len(arr) - 1
    index = -1
    ans = float('inf')
    while low <= high:
        mid = (low + high)//2
        if arr[low] <= arr[high]:
            if arr[low] < ans:
                ans = arr[low]
                index = low
            break
        if arr[low]<=arr[mid]:
            if arr[low] < ans:
                index = low
                ans=  arr[index]
            low = mid + 1
        else:
            if arr[low] < ans:
                index = low
                ans=  arr[index]
            high = mid - 1
    return index

if __name__=='__main__':
    array = [4,5,6,7,0,1,2,3]
    print(countRotation(array))