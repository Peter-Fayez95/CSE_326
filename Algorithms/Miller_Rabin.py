from random import randint

def is_composite(n, a, d, s):
    x = pow(a, d, n)

    if x == 1 or x == n - 1:
        return False
    
    for i in range(1, s):
        x = pow(x, 2, n)
        if x == n - 1:
            return False
    
    return True


def miller_rabin(n, k = 20):

    if n == 1 or n == 4:
        return False
    elif n == 2 or n == 3:
        return True

    s = 0
    d = n - 1
    
    while (d & 1) == 0:
        d >>= 1
        s += 1
    
    for i in range(k):
        a = randint(2, n - 2)

        if is_composite(n, a, d, s):
            return False
        
    return True


# p = 54721083295200779910161477406052586685713892174437

# print(miller_rabin(p))    

    
