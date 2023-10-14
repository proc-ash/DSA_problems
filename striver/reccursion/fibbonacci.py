# Problem Statement: Given an integer N. Print the Fibonacci series up to the Nth term.

def fibbonacciSeries(n):
    if n <= 1:
        return n
    return (fibbonacciSeries(n-1) + fibbonacciSeries(n-2))

if __name__ =='__main__':
    for i in range(10):
        print(fibbonacciSeries(i),end=' ')