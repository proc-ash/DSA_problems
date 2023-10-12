# Problem statement: Given a number ‘N’, find out the sum of the first N natural numbers.

def sumOfNnumbers(n):
    if n == 0:
        return 0
    return n + sumOfNnumbers(n-1)

if __name__ =='__main__':
    print(sumOfNnumbers(5))