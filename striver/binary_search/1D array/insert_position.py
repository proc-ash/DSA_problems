# Problem Statement: You are given a sorted array arr of distinct values and a target value x. 
# You need to search for the index of the target value in the array.
# If the value is present in the array, then return its index. 
# Otherwise, determine the index where it would be inserted in the array while maintaining the sorted order.

def searchPosition(array, target):
    low = 0
    high = len(array) -1
    ans = len(array)
    while low <= high:
        mid = (low + high)//2
        if array[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid +1 
    return ans
if __name__=='__main__':
    array = [1,3,5,7,10]
    print(searchPosition(array, 6))