# Problem Statement: Given an array, print all the elements which are leaders. 
# A Leader is an element that is greater than all of the elements on its right side in the array.

def arrayLeader(array):
    leaders = [array[-1]]
    max_element = array[-1]
    for index in range(len(array)-2,-1,-1):
        if array[index] > max_element:
            leaders.insert(0,array[index])
            max_element = array[index]
    return leaders

if __name__ =='__main__':
    array = [10,22,12,3,0,6]
    print(arrayLeader(array))