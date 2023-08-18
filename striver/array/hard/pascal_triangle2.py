# Variation 2: Given the row number n. Print the n-th row of Pascal’s triangle.


def pascalTriangle(row):
    row -= 1
    result = [1]
    temp = 1
    for i in range(0,row):
        temp *= row-i
        temp /= i+1
        result.append(int(temp))
    return result

if __name__=='__main__':
    print(pascalTriangle(5))
