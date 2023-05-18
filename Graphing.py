import matplotlib.pyplot as plt

from prime_properties import mersenne_prime, pythagorean_prime, \
additive_prime, sophie_germain_prime, is_twin_pair 

from Algorithms.Fermat_Test import fermat
from Algorithms.Miller_Rabin import miller_rabin



start = 3 
end = 200
prev_p = 2
step = 10

cnt_primes = 0
cnt_mersennes = 0
cnt_twin_pairs = 0
cnt_sophie_germain = 0
cnt_pythagorean = 0
cnt_additive = 0

y_density = []
y_mersennes = []
y_twin_pairs = []
y_sophie_germain = []
y_pythagorean = []
y_additive = []

x = [i * step for i in range(1, end + 1)]

for i in range(start, end + 1):
    if fermat(i) and miller_rabin(i):
        cnt_primes += 1

        if mersenne_prime(i):
            cnt_mersennes += 1
        
        if is_twin_pair(i, prev_p):
            cnt_twin_pairs += 1

        if additive_prime(i):
            cnt_additive += 1
          
        if sophie_germain_prime(i):
            cnt_sophie_germain += 1

        if pythagorean_prime(i):
            cnt_pythagorean += 1

        prev_p = i
    
    if i % step == 0:
        y_density.append(cnt_primes)
        y_additive.append(cnt_additive)
        y_mersennes.append(cnt_mersennes)
        y_pythagorean.append(cnt_pythagorean)
        y_sophie_germain.append(cnt_sophie_germain)
        y_twin_pairs.append(cnt_twin_pairs)

        cnt_primes = 0
        cnt_additive = 0
        cnt_mersennes = 0
        cnt_twin_pairs = 0
        cnt_sophie_germain = 0
        cnt_pythagorean = 0


plt.plot(x, y_density)

