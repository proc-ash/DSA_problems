# Problem: Print from N to 1 using Recursion

def nTo1(n):
    if n == 0:
        return 
    print(n)
    nTo1(n-1)
if __name__ =='__main__':
    nTo1(10)
