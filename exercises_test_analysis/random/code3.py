def gcd(a, b):
    """
    Euclid’s Algorithm - GCD
    The idea of the algorithm is based on the observation that,
    if r is the remainder when a is divided by b, then the common
     divisors of a and b are precisely the same as the common
     divisors of b and r
    GCD(206, 40) = GCD(40,6)
                 = GCD(6,4)
                 = GCD(4,2)
                 = GCD(2,0)
                 = 2
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)