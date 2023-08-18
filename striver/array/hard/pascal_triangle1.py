# Variation 1: Given row number r and column number c. Print the element at position (r, c) in Pascal’s triangle.
# Input Format: N = 5, r = 5, c = 3
# Result: 6 
# In Pascal’s triangle, each number is the sum of the two numbers directly above it as shown in the figure below:
# 1 
# 1 1 
# 1 2 1 
# 1 3 3 1 
# 1 4 6 4 1
def pascalTriangle(row, col):
    row -= 1
    col -= 1
    result = 1
    for i in range(col):
        result *= row-i
        result /= i+1
    return int(result)

if __name__=='__main__':
    print(pascalTriangle(40,4))
