# Problem Statement: Given a matrix if an element in the matrix is 0 
# then you will have to set its entire column and row to 0 and then return the matrix.

def zeroMatrix(array):
    col0 = 1
    rows = len(array)
    columns = len(array[0])
    for row in range(rows):
        for column in range(columns):
            if array[row][column] == 0:
                array[row][0] = 0

                if column != 0:
                    array[0][column] = 0
                else:
                    col0 = 0
        for column in range(1,columns):
            for row in range(1,rows):
                if array[row][column] != 0:
                    if array[row][0] == 0 or array[0][column] == 0:
                        array[row][column] = 0
        if array[0][0] ==0:
            for column in range(columns):
                array[0][column]=0
            if col0 == 0:
                for row in range(rows):
                    array[row][0] =0
        return array

if __name__ == '__main__':
    array = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    zeroMatrix(array)
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j], end=' ')
        print(end='\n')