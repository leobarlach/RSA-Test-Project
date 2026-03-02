from primes import generate_large_prime
import math

def extended_gcd(a, b):
    """
    Returns (gcd, x, y) such that a*x + b*y = gcd(a, b)
    Useful for finding the modular inverse.
    """
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def modular_inverse(e, phi):
    """
    Finds the modular inverse of e modulo phi.
    Returns d such that (e * d) % phi == 1
    """
    gcd, x, y = extended_gcd(e, phi)
    if gcd != 1:
        raise Exception("Modular inverse does not exist")
    else:
        return x % phi

def generate_keypair(keysize=255):
    """
    Generates a public and private RSA key pair.
    keysize corresponds to the number of bits in the primes p and q.
    """
    # 1. Generate two distinct large primes, p and q.
    p = generate_large_prime(keysize)
    q = generate_large_prime(keysize)
    while p == q:
        q = generate_large_prime(keysize)
        
    # 2. Compute n = p * q
    n = p * q
    
    # 3. Compute Euler's totient function: phi(n) = (p-1)*(q-1)
    phi = (p - 1) * (q - 1)
    
    # 4. Choose an integer e such that 1 < e < phi AND gcd(e, phi) = 1
    # A common choice is 65537, but we can also search for one
    e = 65537
    if math.gcd(e, phi) != 1:
        # Fallback if 65537 happens to share a factor with phi
        e = 3
        while math.gcd(e, phi) != 1:
            e += 2
            
    # 5. Determine d as d = e^-1 mod phi
    d = modular_inverse(e, phi)
    
    # Return (public_key, private_key) as tuples
    # Public key is (e, n) and Private key is (d, n)
    return ((e, n), (d, n))

if __name__ == "__main__":
    print("Generating RSA Keypair...")
    public_key, private_key = generate_keypair(255)
    
    e, n = public_key
    d, _ = private_key
    
    print("\nPublic Key:")
    print(f"e = {e}")
    print(f"n = {n}")
    
    print("\nPrivate Key:")
    print(f"d = {d}")
    
    print(f"\nBit length of n: {n.bit_length()}")
