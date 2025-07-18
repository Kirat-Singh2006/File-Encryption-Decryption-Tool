
import os
from cryptography.fernet import Fernet
# Banner
from datetime import datetime
from colorama import init, Fore, Style

init()

banner = (
    "\033[38;5;205m"  # Start bright pink
    r"""
  _____                _____        ______  _____   ______         _____    ____   ____ 
 |\    \   _____   ___|\    \   ___|\     \|\    \ |\     \    ___|\    \  |    | |    |
 | |    | /    /| |    |\    \ |     \     \\\    \| \     \  /    /\    \ |    | |    |
 \/     / |    || |    | |    ||     ,_____/|\|    \  \     ||    |  |    ||    |_|    |
 /     /_  \   \/ |    |/____/ |     \--'\_|/ |     \  |    ||    |  |____||    .-.    |
|     // \  \   \ |    |\    \ |     /___/|   |      \ |    ||    |   ____ |    | |    |
|    |/   \ |    ||    | |    ||     \____|\  |    |\ \|    ||    |  |    ||    | |    |
|\ ___/\   \|   /||____| |____||____ '     /| |____||\_____/||\ ___\/    /||____| |____|
| |   | \______/ ||    | |    ||    /_____/ | |    |/ \|   ||| |   /____/ ||    | |    |
 \|___|/\ |    | ||____| |____||____|     | / |____|   |___|/ \|___|    | /|____| |____|
    \(   \|____|/   \(     )/    \( |_____|/    \(       )/     \( |____|/   \(     )/  
     '      )/       '     '      '    )/        '       '       '   )/       '     '
"""
    "\033[0m"  # Reset color
)

print(banner)

print(Fore.WHITE + "\n****************************************************************")
print("*  Copyright of wrench project, 2025                           *")
print(f"*  Loaded at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}                *")
print("****************************************************************" + Style.RESET_ALL)

# Step 1: Load the saved key
with open("secret.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

# Step 2: Define target directory
target_dir = r"C:\Users\home\OneDrive\Desktop\sandbox"

# Step 3: Walk through files and decrypt them
for root, dirs, files in os.walk(target_dir):
    for filename in files:
        # Skip ransom note and key file
        if filename in ("README_RECOVER_FILES.txt", "secret.key"):
            continue

        file_path = os.path.join(root, filename)

        with open(file_path, "rb") as f:
            encrypted_data = f.read()

        decrypted_data = cipher.decrypt(encrypted_data)

        with open(file_path, "wb") as f:
            f.write(decrypted_data)

print("Decryption complete.")
