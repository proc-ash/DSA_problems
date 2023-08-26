# Problem Statement: Given a sorted array of N integers and an integer x, write a program to find the lower bound of x.
def lowerBound(arr: [int], n: int, x: int) -> int:
    # Write your code here
    low, high = 0, n-1
    ans = n
    while low <= high:
        mid = (low + high)//2
        if arr[mid] >= x:
            ans = mid

            high = mid -1
        else:
            low = mid + 1
    return ans

if __name__ =='__main__':
    array = [1,2,2,3]
    print(lowerBound(array, 4, 2))
