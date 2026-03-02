import streamlit as st
from st_copy_to_clipboard import st_copy_to_clipboard

# Import functions from existing modules
from rsa_keys import generate_keypair
from rsa_cipher import encrypt, decrypt

st.set_page_config(page_title="RSA Cryptography Suite", layout="wide")

# Initialize session state for keys
if "generated_d" not in st.session_state:
    st.session_state.generated_d = ""
if "generated_e" not in st.session_state:
    st.session_state.generated_e = ""
if "generated_n" not in st.session_state:
    st.session_state.generated_n = ""

def generate_new_keys():
    # We will use 255-bit keys by default based on main.py
    public_key, private_key = generate_keypair(255)
    st.session_state.generated_e = str(public_key[0])
    st.session_state.generated_n = str(public_key[1])
    st.session_state.generated_d = str(private_key[0])

st.title("🛡️ RSA Cryptography Suite")

st.markdown("""
> ⚠️ **Notice**
> 
> This application was created as a coding exercise to test the capabilities of Google's agentic coding tool, Anti Gravity. **It is not meant to be a secure encryption tool and should only be used for fun or educational purposes.**
>
> **Author:** [Leo Barlach](https://www.linkedin.com/in/leo-barlach/)
""")

# Toggle for mode selection
mode = st.radio("Select Mode:", ["Receiving Message", "Sending Message"], horizontal=True)

st.markdown("---")

if mode == "Receiving Message":
    st.header("Receiving Message (Decrypt)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Key Management")
        
        # Option choice
        key_option = st.radio("Choose an option:", ["Generate New Keys", "Use Previously Generated Key"])
        
        if key_option == "Generate New Keys":
            st.write("Generate a new pair of RSA keys.")
            
            # Initial generation if not yet generated
            if st.session_state.generated_e == "":
                generate_new_keys()
                
            if st.button("Regenerate Random Value"):
                generate_new_keys()
            
            st.markdown("#### Public Key (Share this!)")
            st.info(f"**e:** {st.session_state.generated_e}\n\n**n:** {st.session_state.generated_n}")
            public_key_str = f"The Public Keys are:\nPublic exponent (e): {st.session_state.generated_e}\nmodulus (n): {st.session_state.generated_n}"
            st_copy_to_clipboard(public_key_str, "Copy Public Key to Clipboard", "Copied!")
            
            st.markdown("#### Private Key (Keep Secret!)")
            st.error(f"**d:** {st.session_state.generated_d}\n\n**n:** {st.session_state.generated_n}")
            private_key_str = f"The Private Keys are:\nPrivate exponent (d): {st.session_state.generated_d}\nmodulus (n): {st.session_state.generated_n}"
            st_copy_to_clipboard(private_key_str, "Copy Private Key to Clipboard", "Copied!")
            
            # Use these keys for decryption
            working_d = st.session_state.generated_d
            working_n = st.session_state.generated_n
            
        else:
            st.write("Enter your existing Private Key components to decrypt a message.")
            working_d = st.text_input("Enter your Private exponent (d):")
            working_n = st.text_input("Enter your modulus (n):")

    with col2:
        st.subheader("Message Decryption")
        ciphertext_str = st.text_area("Encrypted Message (Ciphertext Integer):", height=200)
        
        if st.button("Decrypt Message"):
            if not ciphertext_str.strip():
                st.warning("Please enter an encrypted message to decrypt.")
            elif not working_d or not working_n:
                st.warning("Ensure your private key (d, n) is provided or generated!")
            else:
                try:
                    d = int(working_d)
                    n = int(working_n)
                    ciphertext = int(ciphertext_str.strip())
                    
                    decrypted_message = decrypt((d, n), ciphertext)
                    st.success("Message Successfully Decrypted!")
                    st.text_area("Decrypted Message:", value=decrypted_message, height=150, disabled=True)
                except ValueError:
                    st.error("Invalid input. Ciphertext and keys must be valid integers.")
                except Exception as e:
                    st.error(f"Failed to decrypt message: {e}")

elif mode == "Sending Message":
    st.header("Sending Message (Encrypt)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Recipient's Public Key")
        st.write("Enter the public key of the person you are sending a message to.")
        working_e = st.text_input("Enter Public exponent (e):")
        working_n = st.text_input("Enter modulus (n):")
        
    with col2:
        st.subheader("Message Encryption")
        
        # Determine max chars dynamically if 'n' is provided
        max_bytes = 60 # Default safe fallback
        if working_n and working_n.isdigit():
            n_int = int(working_n)
            max_bytes = (n_int.bit_length() - 1) // 8
        
        st.write(f"*(Max size approximately {max_bytes} characters for your key size)*")
        
        plaintext = st.text_area("Enter your message:", max_chars=max_bytes, height=200)
        
        if st.button("Generate Encrypted Text"):
            if not plaintext.strip():
                st.warning("Please write a message to encrypt.")
            elif not working_e or not working_n:
                st.warning("Please provide the recipient's public key (e, n).")
            else:
                try:
                    e = int(working_e)
                    n = int(working_n)
                    
                    encrypted_int = encrypt((e, n), plaintext)
                    
                    st.success("Message Encrypted Successfully!")
                    encrypted_msg_str = str(encrypted_int)
                    
                    st.text_area("Encrypted Message (Send this):", value=encrypted_msg_str, height=150, disabled=True)
                    st_copy_to_clipboard(encrypted_msg_str, "Copy Encrypt Text to Clipboard", "Copied!")
                    
                except ValueError:
                    st.error("Invalid public key. Ensure 'e' and 'n' are integers.")
                except Exception as ex:
                    st.error(f"Failed to encrypt message: {ex}")
