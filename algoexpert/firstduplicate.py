# write a function that returns the first duplicate value occurs in an array

def firstDuplicateValue(array):
    for element in array:
        element = abs(element)
        if array[element - 1] < 0:
            return element
        else:
            array[element - 1] *= -1
    return -1

if __name__ == "__main__":
     array = [2, 1, 5, 2, 3, 3, 4]
     print(firstDuplicateValue(array))
