# Pattern-15: Reverse Letter Triangle Pattern
# A B C D E F
# A B C D E 
# A B C D
# A B C
# A B
# A
n = int(input('number: '))
start = 65
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(chr(start),end=' ')
        start +=1
    start = 65
    print('')
