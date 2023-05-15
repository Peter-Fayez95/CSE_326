from random import randint

def fermat(n, k = 20):
    
    if n == 1 or n == 4:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        for i in range (k) :
            a = randint(2, n - 2)
            if pow (a , n -1 , n ) != 1:
                return False
    return True

# p = 15240934928185218396651602424881890246060448594959

# print(fermat(p))
