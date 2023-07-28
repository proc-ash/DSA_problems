# given an array of integer and an integer. Write a function that moves all the 
# instance of that integer to end of the array
def moveElementToEnd(array, toMove):
    to_move_index = 0
    index = 0

    while index < len(array):
        if array[index] != toMove:
            if array[to_move_index] == toMove:
                array[index], array[to_move_index] = array[to_move_index], array[index]
            to_move_index += 1
        index += 1
    return array

if __name__ == '__main__':
    array = [1, 2, 4, 5, 3]
    toMove = 3
    print(moveElementToEnd(array, toMove))
