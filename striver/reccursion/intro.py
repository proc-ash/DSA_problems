def recursion(count):
    if count == 3:
        return
    print(count)
    count +=1
    recursion(count)

if __name__ =='__main__':
    count  = 0
    recursion(count)