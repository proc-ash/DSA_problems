# Pattern – 17: Alpha-Hill Pattern

#      A     
#     ABA    
#    ABCBA   
#   ABCDCBA  
#  ABCDEDCBA 
# ABCDEFEDCBA 

n = int(input('number: '))
start = 65
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(' ',end='')
    for j in range(1,i+1):
        print(chr(start),end='')
        start +=1
    start -=2
    for j in reversed(range(1,i)):
        print(chr(start),end='')
        start -=1
    start = 65
    for j in range(1,n-i+1):
        print(' ',end='')
    print('')
