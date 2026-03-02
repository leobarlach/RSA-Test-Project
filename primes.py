import random

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
    First checks divisibility against small primes (<= 100),
    then runs the Miller-Rabin test.
    """
    small_primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
        31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 
        73, 79, 83, 89, 97
    ]
        
    for p in small_primes:
        if x % p == 0:
            return False
            
    # If not divisible by any small primes, run Miller-Rabin
    return miller_rabin_test(x)

def generate_large_prime(n=255):
    """
    Generates a large prime number starting from a random n-bit number.
    Uses n=255 bits by default.
    """
    # Create a random number with n binary digits
    rand_num = random.getrandbits(n)
    
    # Take 2*rand_num + 1 to assure the number is odd
    candidate = 2 * rand_num + 1
    
    # If not prime, add 2 and try again
    while not check_if_prime(candidate):
        candidate += 2
        
    return candidate

if __name__ == "__main__":
    print("Generating a large prime...")
    prime = generate_large_prime(255)
    print(f"Generated Prime:\n{prime}")
    print(f"\nBit length: {prime.bit_length()}")
