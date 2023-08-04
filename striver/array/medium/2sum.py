# Problem Statement: Given an array of integers arr[] and an integer target.

# 1st variant: Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.

# 2nd variant: Return indices of the two numbers such that their sum is equal to the target. Otherwise, we will return {-1, -1}.

def twoSum(array, target):
    count = {}
    for element in array:
        if target - element not in count.keys():
            count[element] = True
        else:
            return [element, target-element]
    return [-1,-1]

if __name__ == '__main__':
    array = [4,8,7,3,2,9]
    print(twoSum(array,10))