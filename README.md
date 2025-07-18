# File-Encryption-Decryption-Tool
File Encryption & Decryption Tool

This Python-based tool simulates a ransomware-like environment by encrypting and decrypting files in a target directory using symmetric encryption (Fernet). It is strictly for educational, testing, or training purposes such as cyber range labs or blue team readiness.
⚠️ Legal Disclaimer

This project is NOT malware and does not exfiltrate or demand ransom. It is a simulation designed for ethical, controlled environments. Do not deploy this script on any system you do not own or without explicit permission. Unauthorized use is illegal.
🧾 Overview

This project includes two core scripts:
1. 🔒 encrypt_files.py

    Generates a Fernet encryption key and stores it in secret.key

    Recursively encrypts all files in the specified directory

    Skips the key file to avoid encrypting itself

    Drops a fake ransom note (README_RECOVER_FILES.txt)

2. 🔓 decrypt_files.py

    Loads the secret.key

    Recursively decrypts all encrypted files in the directory

    Skips the ransom note and key file

Both scripts display a themed ASCII banner with timestamps as part of the fictional "Wrench Project" branding.
