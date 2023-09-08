# Problem Statement: Given two numbers N and M, find the Nth root of M. 
# The nth root of a number M is defined as a number X when raised to the power N equals M. 
# If the ‘nth root is not an integer, return -1.

def NthRoot(n: int, m: int) -> int:
    # Write Your Code Here
    if m==0 or n==1:
        return m
    low= 1
    high = m
    while low <= high:
        mid = (low + high)//2
        if mid**n == m:
            return mid
        elif mid**n< m:
            low = mid +1
        else:
            high = mid-1
    return -1
if __name__=='__main__':
    n= 3
    m= 100
    print(NthRoot(n,m))