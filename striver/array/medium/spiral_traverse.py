# Problem Statement: Given a Matrix, print the given matrix in spiral order.

def traverseSpiral(matrix):
    top, bottom, left, right = 0,len(matrix) - 1,0, len(matrix[0]) - 1
    result = []

    while (left <= right and top <= bottom):
        
        #travelling from left to right
        
        for index in range(left,right + 1):
            result.append(matrix[top][index])
        top += 1

        # from moving top to bottom
        for index in range(top, bottom+1):
            result.append(matrix[index][right])
        right -= 1

        # from moving right to left
        if (top <= bottom):
            for index in range(right, left-1, -1):
                result.append(matrix[bottom][index])
            bottom -= 1
        #from moving bottom to top
        if (left <= right):
            for index in range(bottom, top-1,-1):
                result.append(matrix[index][left])
            left += 1
    return result

if __name__ == '__main__':
    array = [[1,2,3],[8,9,4],[7,6,5]]
    print(traverseSpiral(array))
