def firstAndLastPosition(nums, n, target):
    # Write your code here
    def search(target):
        low = 0
        high = n
        while low < high:
            mid = (low + high)//2
            if nums[mid]<target:
                low = mid + 1
            else:
                high = mid
        return low
    first = search(target)
    last = search(target+1)-1

    if first <= last:
        return [first, last]
    return [-1, -1]

if __name__=='__main__':
    array = [1,2,5,7,7,8,8,9,9,9,9,10,15]
    print(firstAndLastPosition(array,len(array), 9))