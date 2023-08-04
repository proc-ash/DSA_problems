# Problem Statement: Given an array of N integers, write a program to return an element that occurs more than N/2 times 
# in the given array. You may consider that such an element always exists in the array.

def majorityElement(array):
    count = 0
    answer = None

    for value in array:
        if count == 0:
            answer = value
        if value == answer:
            count += 1
        else:
            count -= 1
    return answer

if __name__ =='__main__':
    array = [4,4,2,4,3,4,4,3,2,4]
    print(majorityElement(array))