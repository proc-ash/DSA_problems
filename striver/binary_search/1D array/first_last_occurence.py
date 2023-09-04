
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
    array = [0,0,1,1,2,2,2,2]
    print(firstAndLastPosition(array,len(array), 2))