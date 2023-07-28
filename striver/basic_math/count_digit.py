# Given a number N. Count the number of digits in N which evenly divides N.


def count_digit(n):
    count = 0
    temp = n
    while n > 0:
        rem = n%10
        if rem != 0:
            if temp % rem == 0:
                count += 1
        n = n/10
    return count
n = int(input('enter the number: '))
print(count_digit(n))