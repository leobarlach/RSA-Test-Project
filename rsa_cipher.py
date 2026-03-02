from rsa_keys import generate_keypair

def encrypt(public_key, plaintext):
    """
    Encrypts a string plaintext using the public key (e, n).
    """
    e, n = public_key
    
    # Convert the string to bytes, then to an integer representation
    plain_bytes = plaintext.encode('utf-8')
    plain_int = int.from_bytes(plain_bytes, byteorder='big')
    
    if plain_int >= n:
        raise ValueError("Message is too large for the key size.")
        
    # RSA Encryption formula: C = P^e mod n
    cipher_int = pow(plain_int, e, n)
    
    return cipher_int

def decrypt(private_key, ciphertext):
    """
    Decrypts an integer ciphertext using the private key (d, n).
    """
    d, n = private_key
    
    # RSA Decryption formula: P = C^d mod n
    plain_int = pow(ciphertext, d, n)
    
    # Convert the integer back to bytes, then decode to string
    # Calculate the number of bytes required to hold the integer
    byte_length = (plain_int.bit_length() + 7) // 8
    
    # Handle the edge case where the message was exactly 0
    if byte_length == 0:
        plain_bytes = plain_int.to_bytes(1, byteorder='big')
    else:
        plain_bytes = plain_int.to_bytes(byte_length, byteorder='big')
        
    plaintext = plain_bytes.decode('utf-8')
    
    return plaintext

if __name__ == "__main__":
    print("Generating RSA Keypair (255-bit primes)...")
    public_key, private_key = generate_keypair(255)
    
    print("Keys generated successfully!\n")
    
    # A test message
    message = "Hello RSA! This is a test message to practice coding."
    print(f"Original Message:\n'{message}'\n")
    
    # Encrypt
    encrypted_msg = encrypt(public_key, message)
    print(f"Encrypted Message (Ciphertext Integer):\n{encrypted_msg}\n")
    
    # Decrypt
    decrypted_msg = decrypt(private_key, encrypted_msg)
    print(f"Decrypted Message:\n'{decrypted_msg}'\n")
    
    # Verify correctness
    if message == decrypted_msg:
        print("SUCCESS! The decrypted message matches the original.")
    else:
        print("ERROR! The decrypted message does not match.")
