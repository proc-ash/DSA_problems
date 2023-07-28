#givven an non-empty array and target sum return all triplets that sum upto the targetSum in sorted order

def threeNumberSum(array, targetSum):
    array.sort()
    result =[]
    left_index = 0
    right_index = len(array) - 1
    while left_index < right_index:
        if right_index - 1 == left_index:
            left_index +=1
            right_index = len(array) -1
        if left_index +1 == len(array) -1 :
            break
        for i in range(left_index+1, right_index):
            if (array[left_index] + array[i] + array[right_index]) == targetSum:
                result.append([array[left_index], array[i], array[right_index]])
        right_index -=1
    return result

if __name__ == '__main__':
    array = [12, 3, 1, 2, -6, 5, 0, -8, -1]
    targetSum = 0
    print(threeNumberSum(array, targetSum))

