# Problem: Print your Name N times using recursion

def name(i,n):
    if i >= n:
        return
    print(f"My name Prakash is being printed for {i+1} time")
    i += 1
    name(i,n)

if __name__=='__main__':
    name(i=0,n = 5)
