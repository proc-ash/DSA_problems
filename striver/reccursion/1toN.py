# Problem: Print from 1 to N using Recursion

def oneToN(i,n):
    if i > n:
        return
    print(i)
    oneToN(i+1, n)
if __name__ =='__main__':
    oneToN(1,10)
