# write a function that takes an non-empty array of ineteger and returns
# an array of same length where each element in the output array is equal to the product of every number in input array

def arrayOfProduct(array):
    result = [1] * len(array)
    left_product = 1
    for i in range(len(array)):
        result[i] = left_product
        left_product *= array[i]
    right_product = 1
    for i in reversed(range(len(array))):
        result[i] *= right_product
        right_product *= array[i]
    return result
if __name__ == '__main__':
    array = [5,1,4,2]
    print(arrayOfProduct(array))