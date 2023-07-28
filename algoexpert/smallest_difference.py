#We are given two arrays of integers. Both of them contain at least one element. 
#We are asked to write a function that is going to find two numbers, one in each array, 
#with the smallest absolute difference, and return them in an array. In the resultant array, 
#the number from the first array should come first.

def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    minimun_difference = float ('inf')
    array1_index = 0
    array2_index = 0
    while array1_index < len(arrayOne) and array2_index < len(arrayTwo):
        current_difference = abs(arrayOne[array1_index] - arrayTwo[array2_index])
        if current_difference < minimun_difference:
            minimun_difference = current_difference
            result = [arrayOne[array1_index], arrayTwo[array2_index]]
        if arrayOne[array1_index] < arrayTwo[array2_index]:
            array1_index +=1
        else:
            array2_index +=1
    return result

if __name__ == '__main__':
    arrayOne = [-1, 5, 10, 20, 28, 3]
    arrayTwo = [26, 134, 135, 15, 17]
    print(smallestDifference(arrayOne, arrayTwo))
    
