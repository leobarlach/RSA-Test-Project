# RSA-Test-Project

Trial project to test Antigravity.

This project is a coding exercise. It relies on a basic implementation of the RSA algorithm (see [RSA cryptosystem on Wikipedia](https://en.wikipedia.org/wiki/RSA_cryptosystem) for more details).

## Features
- Generates RSA public and private keys from prime numbers.
- Encrypts messages using the public key.
- Decrypts messages using the private key.
- Includes a web-based UI built with Streamlit.

## Setup

1. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   
   # Windows
   .venv\Scripts\activate
   
   # Linux/Mac
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To launch the web interface, run the `main.py` script:
```bash
python main.py
```
This will start the Streamlit server and open the RSA Web Application in your default web browser.
