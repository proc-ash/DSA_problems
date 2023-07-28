# Given a 32 bit number X, reverse its binary form and print the answer in decimal.

# Input:
# X = 1
# Output:
# 2147483648 
# Explanation:
# Binary of 1 in 32 bits representation-
# 00000000000000000000000000000001
# Reversing the binary form we get, 
# 10000000000000000000000000000000,
# whose decimal value is 2147483648.

def reverse(x):
    binary_x = '{:032b}'.format(x)
    binary_x = binary_x[::-1]
    return int(binary_x,2)
x = int(input('enter number: '))
print(reverse(x))
