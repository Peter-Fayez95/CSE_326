from Algorithms.Miller_Rabin import miller_rabin
from Algorithms.Fermat_Test import fermat


def digit_sum(x):
    total = 0
    while x > 0:
        total += x % 10
        x /= 10
    return total

def power_of_two(x):
    return (x and (not (x & (x - 1))))

def mersenne_prime(p):
    '''
    Mersenne primes: Have the form p = 2^x - 1
    Mersenne primes (till 200): 2, 3, 5, 7, 13, 17, 19, 31, 
                                61, 89, 107, 127
    '''
    return power_of_two(p + 1)

def is_twin_pair(p, prev_p):
    '''
    A pair of twin primes: two primes with a difference of 2
    Twin prime pairs (till 200): 
            (3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43), (59, 61), 
            (71, 73), (101, 103), (107, 109), (137, 139), (149, 151), 
            (179, 181), (191, 193), (197, 199)
    '''
    return p - prev_p == 2

def sophie_germain_prime(p):
    '''
    Sophie-Germain primes: prime p where 2p + 1 is also a prime
    Sophie-Germain primes (till 200): 2, 3, 5, 11, 23, 29, 41, 53, 83, 
                                      89, 113, 131, 173, 179, 191
    '''
    return fermat(2*p + 1) and miller_rabin(2*p + 1)


def pythagorean_prime(p):
    '''
    Pythagorean primes: Have the form p = 4x + 1
    Pythagorean primes (till 200): 5, 13, 17, 29, 37, 41, 53, 
                                   61, 73, 89, 97, 101, 109, 113, 137, 
                                   149, 157, 173, 181, 193, 197
    '''
    return (p - 1) % 4 == 0


def additive_prime(p):
    '''
    Additive primes: prime p where its digit sum is also a prime
    Additive primes (till 200): 2, 3, 5, 7, 11, 23, 29, 41, 43, 47, 
                                61, 67, 83, 89, 101, 113, 131, 137, 
                                139, 151, 157, 173, 179, 191, 193, 197, 199
    '''
    x = digit_sum(p)
    return fermat(x) and miller_rabin(x)

