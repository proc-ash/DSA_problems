# Pattern – 8: Inverted Star Pyramid

# ***********
#  *********
#   *******
#    ***** 
#     ***    
#      *

n = int(input('number: '))

for i in reversed(range(n)):
    for j in reversed(range(n-i-1)):
        print(' ',end='')
    for j in reversed(range(2*i+1)):
        print('*',end='')
    for j in reversed(range(n-i-1)):
        print(' ',end='')
    print('')
    