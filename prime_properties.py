from Algorithms.Miller_Rabin import miller_rabin
from Algorithms.Fermat_Test import fermat


def digit_sum(x):
    total = 0
    while x>0:
        total += x % 10
        x /= 10
    return total

def power_of_two(x):
    return (x and (not (x & (x - 1))))

def mersenne_prime(p):
    '''
    Mersenne primes: Have the form p = 2^x - 1
    '''
    return power_of_two(p + 1)

def is_twin_pair(p, prev_p):
    '''
    A pair of twin primes: two primes with a difference of 2
    '''
    return p - prev_p == 2

def sophie_germain_prime(p):
    '''
    Sophie-Germain primes: prime p where 2p + 1 is also a prime
    '''
    return fermat(2*p + 1) and miller_rabin(2*p + 1)


def pythagorean_prime(p):
    '''
    Pythagorean primes: Have the form p = 4x + 1
    '''
    return (p - 1) % 4 == 0


def additive_prime(p):
    '''
    Additive primes: prime p where its digit sum is also a prime
    '''
    x = digit_sum(p)
    return fermat(x) and miller_rabin(x)






     