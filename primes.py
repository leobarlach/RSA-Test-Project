import random
import time
import statistics

def miller_rabin_test(n, k=40):
    """
    Miller-Rabin primality test.
    Returns True if n is probably prime, False if it is composite.
    k is the number of iterations (accuracy).
    """
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    
    # Write n-1 as d * 2^s by factoring powers of 2 from n-1
    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d //= 2
        
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
            
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            # If we reach here, it means we didn't break out of the inner loop,
            # so the number is composite.
            return False
            
    return True

def check_if_prime(x):
    """
    Checks if a number x is prime.
    First checks divisibility against small primes (<= 1000),
    then runs the Miller-Rabin test.
    """
    small_primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
        73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
        157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233,
        239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
        331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419,
        421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503,
        509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607,
        613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
        709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811,
        821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911,
        919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997
    ]
        
    for p in small_primes:
        if x % p == 0:
            return False
            
    # If not divisible by any small primes, run Miller-Rabin
    return miller_rabin_test(x)

def generate_large_prime(n=512):
    """
    Generates a large prime number starting from a random n-bit number.
    Uses n=512 bits by default.
    """
    # Create a random number with n-1 binary digits
    rand_num = random.getrandbits(n - 1)
    
    # Take 2*rand_num + 1 to assure the number is odd
    candidate = 2 * rand_num + 1
    
    # If not prime, add 2 and try again
    while not check_if_prime(candidate):
        candidate += 2
        
    return candidate

def test_generation_time():
    bit_sizes = [256, 512, 1024]
    num_trials = 5
    
    print(f"{'Bits':<8} | {'Avg (s)':<10} | {'Median (s)':<10} | {'Min (s)':<10} | {'Max (s)':<10}")
    print("-" * 62)
    
    for bits in bit_sizes:
        times = []
        for _ in range(num_trials):
            start_time = time.time()
            generate_large_prime(bits) 
            end_time = time.time()
            times.append(end_time - start_time)
            
        avg_time = statistics.mean(times)
        med_time = statistics.median(times)
        min_time = min(times)
        max_time = max(times)
        
        print(f"{bits:<8} | {avg_time:<10.4f} | {med_time:<10.4f} | {min_time:<10.4f} | {max_time:<10.4f}")

if __name__ == "__main__":
    test_generation_time()
