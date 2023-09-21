def isRotated(p,q):
    if len(p) != len(q):
        return 0
    for i in range(len(p)):
        if p == q:
            return 1
        p = p[1:] + p[0]
    return 0

if __name__ =='__main__':
    p = 'abac'
    q = 'baca'
    print(isRotated(p,q))