# Problem Statement: Given an array of N integers. Every number in the array except one appears twice. 
# Find the single number in the array.

def singleNonDuplicate(arr):
    # Write your code here
    n= len(arr)
    if n == 1:
        return arr[0]
    if arr[0] != arr[1]:
        return arr[0]
    if arr[n-1] != arr[n-2]:
        return arr[n-1]
    low= 1
    high = n-2
    while low <= high:
        mid = (low + high)//2
        if arr[mid] != arr[mid+1] and arr[mid] != arr[mid-1]:
            return arr[mid]
        if (mid %2 == 0 and arr[mid]== arr[mid+1]) or (mid %2 == 1 and arr[mid]== arr[mid-1]):
            low = mid + 1
        else:
            high = mid -1
    return -1 

if __name__ =='__main__':
    array = [1,1,2,2,3,3,4,5,5,6,6,7,7,8,8]
    print(singleNonDuplicate(array))