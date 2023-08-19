# Problem Statement: Given an array of N integers, your task is to find unique triplets that add up to give a sum of zero. 
# In short, you need to return an array of all the unique triplets [arr[a], arr[b], arr[c]] such that i!=j, j!=k, k!=i, 
# and their sum is equal to zero.

def threeSum(array):
    array.sort()
    result = []
    for i in range(len(array)-2):
        left = i+1
        right = len(array) -1

        while left < right:
            temp = array[i] + array[left] + array[right]
            if temp == 0:
                result.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif temp < 0:
                left += 1
            else:
                right -= 1
    return result

if __name__ =='__main__':
    array = [12, 3, 1, 2, -6, 5, -8, 6]
    print(*threeSum(array))

