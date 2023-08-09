# Problem Statement: Given a matrix, your task is to rotate the matrix 90 degrees clockwise.

# e.g. : 1,2,3      7,4,1
#        4,5,6  ->  8,5,2
#        7,8,9      9,6,3

# This solution can be achieved with two steps:
# first to transpoe the matrix
# second swap the first and last element of the row

def rotateMatrix90(array):
    rows = len(array)
    columns = len(array[0])
# Step 1: Transpoe matrix
    for row in range(rows):
        for column in range(row):
             array[row][column], array[column][row] = array[column][row], array[row][column]

# Step 2: swap the first and last element of the row
    for row in range(rows):
        array[row][0], array[row][len(array[row])-1] = array[row][len(array[row])-1], array[row][0]
    return array

if __name__ =='__main__':
    array = [[1,2,3],[4,5,6],[7,8,9]]
    result = (rotateMatrix90(array))
   
    for i in range(len(result)):
        for j in range(len(result[0])):
            print(result[i][j], end=' ')
        print(end='\n')
