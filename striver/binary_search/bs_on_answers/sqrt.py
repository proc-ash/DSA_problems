# Problem Statement: You are given a positive integer n. 
# Your task is to find and return its square root. If ‘n’ is not a perfect square, 
# then return the floor value of ‘sqrt(n)’.

def findSqrt(n):
    if n == 0 or n == 1:
        return n

    low = 2
    high = n

    while low < high:
        mid = (high+low)//2
        if mid <= (n//mid):
            low = mid + 1
        else:
            high = mid
    return low - 1
if __name__ =='__main__':
    n=11
    print(findSqrt(n))