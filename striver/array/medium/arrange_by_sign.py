# Problem Statement:
# There’s an array ‘A’ of size ‘N’ with an equal number of positive and negative elements. 
# Without altering the relative order of positive and negative elements, 
# you must return an array of alternately positive and negative values.
# Note: Start the array with positive elements.

def arrangeAlternate(array):
    positive, negative = 0, 1
    ans = [0] * len(array)

    for element in array:
        if element < 0:
            ans[negative] = element
            negative += 2
        else:
            ans[positive] = element
            positive += 2
    return ans
if __name__ == '__main__':
    array = [1,2,-4,-5]
    print(arrangeAlternate(array))