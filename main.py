import sys
import subprocess
import os

def main():
    print("Launching the RSA Web Application...")
    try:
        # Check if we are running in a .venv and prefer that python executable for module execution
        # Also prefer to just locate `streamlit` directly if it's on PATH
        
        # Determine the correct python command to use. Using sys.executable is usually safe, 
        # but if the user launched main.py with the wrong Python, let's use the explicit standard.
        python_cmd = sys.executable 
        
        # Execute the module using Streamlit CLI
        subprocess.run([python_cmd, "-m", "streamlit", "run", "app.py"])
        
    except FileNotFoundError:
        print("\n[ERROR] Streamlit not found. Please ensure it is installed in your virtual environment by running:")
        print("pip install streamlit st-copy-to-clipboard")
    except KeyboardInterrupt:
        print("\nRSA Web Application closed.")

if __name__ == "__main__":
    main()
