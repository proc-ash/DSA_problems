# write a function that returns 1D array having elements of a 2D array in spiral form
# [
#   [1, 2, 3, 4],
#   [12, 13, 14, 5],
#   [11, 16, 15, 6],
#   [10, 9, 8, 7]
# ]

def spiralTraverse(array):
    start_row, end_row = 0, len(array)-1
    start_column, end_column = 0, len(array[0])-1
    spiral_array = []
    while start_row <= end_row and start_column <= end_column:
        for column in range(start_column, end_column+1):
            print(array[start_column][column])
            spiral_array.append(array[start_column][column])

        for row in range(start_row + 1, end_row + 1):
            print(array[row][end_column])
            spiral_array.append(array[row][end_column])

        if start_row != end_row:

            for column in reversed(range(start_column, end_column)):
                print(array[end_row][column])
                spiral_array.append(array[end_row][column])

        if start_column != end_column:

            for row in reversed(range(start_row+1, end_row)):
                print(array[row][start_column])
                spiral_array.append(array[row][start_column])
        
        start_row += 1

        end_row += 1

        start_column += 1

        end_column += 1

    return spiral_array

if __name__ == '__main__':

    array =  [
        [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7]
        ]
    print(spiralTraverse(array))