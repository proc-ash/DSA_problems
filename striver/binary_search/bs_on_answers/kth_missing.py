# Problem Statement: You are given a strictly increasing array ‘vec’ and a positive integer ‘k’. 
# Find the ‘kth’ positive integer missing from ‘vec’.

def KthMissing(arr,k):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low + high)//2
        missing = arr[mid] - (mid+1)
        if missing <k:
            low = mid + 1
        else:
            high = mid -1
    #return arr[high] + (k-high)
    return high + k + 1

if __name__=='__main__':
    arr = [2,3,4,7,11]
    k = 4
    print(KthMissing(arr, k))