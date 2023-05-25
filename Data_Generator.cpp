#include <bits/stdc++.h>

using u64 = uint64_t;
using u128 = __uint128_t;
using namespace std;

#define FIn                                                                    \
  cin.tie(0);                                                                  \
  cout.tie(0);                                                                 \
  ios_base::sync_with_stdio(false)

#define file                                                                   \
  freopen("output.txt", "w", stdout);                                             \
  freopen("input.txt", "r", stdin)

int magic_primes[9] = {2, 3, 5, 13, 19, 73, 193, 407521, 299210837};


u64 binpower(u64 base, u64 e, u64 mod) {
    u64 result = 1;
    base %= mod;
    while (e) {
        if (e & 1)
            result = (u128)result * base % mod;
        base = (u128)base * base % mod;
        e >>= 1;
    }
    return result;
}

bool check_composite(u64 n, u64 a, u64 d, int s) {
    u64 x = binpower(a, d, n);
    if (x == 1 || x == n - 1)
        return false;
    for (int r = 1; r < s; r++) {
        x = (u128)x * x % n;
        if (x == n - 1)
            return false;
    }
    return true;
};

bool miller_rabin(u64 n) { // returns true if n is  prime, else returns false.
    if (n < 4)
        return n == 2 || n == 3;
    
    if (binary_search(magic_primes,magic_primes+9,n)) {
        return 1;
    }

    int s = 0;
    u64 d = n - 1;
    while ((d & 1) == 0) {
        d >>= 1;
        s++;
    }

    for (int i :{2, 325, 9375, 28178, 450775, 9780504, 1795265022}) {
        if (check_composite(n, i, d, s))
            return false;
    }
    return true;
}


int digit_sum(u64 x) {
    int tot = 0;
    while (x > 0) {
        tot += (x % 10);
        x /= 10;
    }
    return tot;
} 


bool power_of_two(u64 x) {
    return x && (!(x & (x - 1)));
}


bool mersenne_prime(u64 p) {
    return power_of_two(p + 1);
}

bool is_twin_pair(u64 p, u64 prev_p) {
    return p - prev_p == 2;
}

bool sophie_germain_prime(u64 p) {
    return miller_rabin(2*p + 1);
}

bool pythagorean_prime(u64 p) {
    return (p - 1) % 4 == 0;
}

bool additive_prime(u64 p) {
    int x = digit_sum(p);
    return miller_rabin(x);
}





int main(){
    FIn;
    file;
    clock_t c_start = clock();
    cout<<"range,density,twins,mersenne,germain,pythagorean,additive\n";
    
    long long cnt_primes = 1, \
    cnt_mersennes = 0,\
    cnt_twin_pairs = 0,\
    cnt_sophie_germain = 0,\
    cnt_pythagorean = 0,\
    cnt_additive = 0;

    u64 prev_p = 2;

    for (u64 i = 3; i <= 1e10; i+=2) {
        if (miller_rabin(i)) {
            cnt_primes++;

            if (mersenne_prime(i))
                cnt_mersennes += 1;
            
            if (is_twin_pair(i, prev_p))
                cnt_twin_pairs += 1;

            if (additive_prime(i))
                cnt_additive += 1;
            
            if (sophie_germain_prime(i))
                cnt_sophie_germain += 1;

            if (pythagorean_prime(i))
                cnt_pythagorean += 1;
        
        prev_p = i;
        }

        if ((i+1) % 100000 == 0) {

            cout<<i<<","<<cnt_primes<<","<<cnt_twin_pairs<<","\
            <<cnt_mersennes<<","<<cnt_sophie_germain<<","<<cnt_pythagorean\
            <<","<<cnt_additive<<"\n";
        }
    }

    cout << 1000.0 * (clock() - c_start) / CLOCKS_PER_SEC;
}
