# bubble sort
# swap adjecent elements until the greates one is moved to the last index


def bubbleSort(array):
    for iteration in range(len(array)):
        for next_element in range(1,len(array)-iteration):
            if array[next_element] < array[next_element - 1]:
                array[next_element], array[next_element -1] = array[next_element - 1], array[next_element]

if __name__ == '__main__':
    array = [7,6,1,5,4,9,2]
    bubbleSort(array)
    print(array)