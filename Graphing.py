import matplotlib.pyplot as plt, csv

from prime_properties import mersenne_prime, pythagorean_prime, \
additive_prime, sophie_germain_prime, is_twin_pair 

from Algorithms.Fermat_Test import fermat
from Algorithms.Miller_Rabin import miller_rabin



start = 3 
end = 200
prev_p = 2
step = 10
num_steps = end // step

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

x = [i * step for i in range(1, num_steps + 1)]

file = open("primes.csv", 'w') 
writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator = '\n')
writer.writerow(["density","twins","mersenne","germain","pythagorean","additive"])        

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
        
        writer.writerow([f"{cnt_primes}", f"{cnt_twin_pairs}", f"{cnt_mersennes}", 
                         f"{cnt_sophie_germain}", f"{cnt_pythagorean}", f"{cnt_additive}"])

        cnt_primes = 0
        cnt_additive = 0
        cnt_mersennes = 0
        cnt_twin_pairs = 0
        cnt_sophie_germain = 0
        cnt_pythagorean = 0

file.close()

fig1, ax1 = plt.subplots()
ax1.plot(x, y_density, color='red')
ax1.set_xlabel("Prime Density")
#plt.savefig('Density.jpg')

fig2, ax2 = plt.subplots()
ax2.plot(x, y_twin_pairs, color='red')
ax2.set_xlabel("Twin Primes Density")
#plt.savefig("Twin Primes.jpg")

fig3, ax3 = plt.subplots()
plt.plot(x, y_mersennes, color='red')
ax3.set_xlabel("Mersenne Primes Density")
#plt.savefig("Mersenne Primes.jpg")

fig4, ax4 = plt.subplots()
plt.plot(x, y_sophie_germain, color='red')
ax4.set_xlabel("Sophie-Germain Primes Density")
#plt.savefig("Sophie_Germain Primes.jpg")

fig5, ax5 = plt.subplots()
plt.plot(x, y_pythagorean, color='red')
ax5.set_xlabel("Pythagorean Primes Density")
#plt.savefig("Pythagorean Primes")

fig6, ax6 = plt.subplots()
plt.plot(x, y_additive, color='red')
ax6.set_xlabel("Additive Primes Density")
#plt.savefig("Additive Primes.jpg")
