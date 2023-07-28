#given a 2d array write a function that transpose the give matrix

def transposeMatrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    transposed_matrix = []
    for column in range(columns):
        temp_arr =[]
        for row in range(rows):
            temp_arr.append(matrix[row][column])
        transposed_matrix.append(temp_arr)
    return transposed_matrix

if __name__ == '__main__':
    matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
  ]
    print(transposeMatrix(matrix),end='\n')