# Problem Statement: You are given an array. The task is to reverse the array and print it. 
def arrayReverse(start, end, nums):
    if start < end:
        nums[start], nums[end] = nums[end], nums[start]
        arrayReverse(start+1, end -1, nums)
if __name__=='__main__':
    n=5
    nums = [7,5,3,2,1]
    print('Befor reversing: ',nums)
    arrayReverse(0,n-1,nums)
    print('After reversing',nums)