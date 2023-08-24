# Problem Statement: You are given a read-only array of N integers with values also in the range [1, N] both inclusive.
# Each integer appears exactly once except A which appears twice and B which is missing. 
# The task is to find the repeating and missing numbers A and B where A repeats twice and B is missing.

def repeatingMissingArray(a):
    n = len(array)
    SN = (n * (n + 1)) // 2
    S2N = (n * (n + 1) * (2 * n + 1)) // 6

    # Calculate S and S2:
    S, S2 = 0, 0
    for i in range(n):
        S += a[i]
        S2 += a[i] * a[i]

    # S-Sn = X-Y:
    val1 = S - SN

    # S2-S2n = X^2-Y^2:
    val2 = S2 - S2N

    # Find X+Y = (X^2-Y^2)/(X-Y):
    val2 = val2 // val1

    # Find X and Y: X = ((X+Y)+(X-Y))/2 and Y = X-(X-Y),
    # Here, X-Y = val1 and X+Y = val2:
    x = (val1 + val2) // 2
    y = x - val1

    return [x, y]




if __name__ == '__main__':
    array = [3,1,2,5,3]
    print(repeatingMissingArray(array))

