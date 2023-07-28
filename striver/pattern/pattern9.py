# Pattern – 9: Diamond Star Pattern
#      *
#     ***
#    ***** 
#   *******
#  *********
# ***********  
# ***********
#  *********
#   *******
#    ***** 
#     ***    
#      *

n = int(input('number: '))
for i in range(n):
    for j in range(n-i-1):
        print(' ',end='')
    for j in range(2*i+1):
        print('*',end='')
    for j in range(n-i-1):
        print(' ',end='')
    print('')
for i in reversed(range(n)):
    for j in reversed(range(n-i-1)):
        print(' ',end='')
    for j in reversed(range(2*i+1)):
        print('*',end='')
    for j in reversed(range(n-i-1)):
        print(' ',end='')
    print('')
