# Problem Statement: You are given a sorted array containing N integers and a number X, 
# you have to find the occurrences of X in the given array.

def count(arr: [int], n: int, x: int) -> int:
    # Your code goes here
    def search(x):
        low= 0
        high = n
        while low < high:
            mid = (low + high) // 2
            if x > arr[mid]:
                low= mid + 1
            else:
                high = mid
        return low
    first= search(x)
    last = search(x+1)

    return last-first

if __name__=='__main__':
    array = [1, 1, 2, 2, 2, 2, 2, 3]
    print(count(array, len(array), 2))