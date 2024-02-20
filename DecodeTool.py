
from cryptography.fernet import Fernet
import os

def search_file(directory:str, extension:list):
    files_found = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(tuple(extension)):
                files_found.append(os.path.join(root, file))
    return files_found

key = input("Input key\n\n").encode()
encrypted_files = search_file('C:\\test', ['.hacked'])

cipher = Fernet(key)
for encrypted_file in encrypted_files:
    decrypted_file = (encrypted_file.rsplit('.hacked',1))[0]

    with open(encrypted_file, "rb") as encrypted_target:
        decrypted_data = cipher.decrypt(encrypted_target.read())
        with open(decrypted_file, "wb") as decrypted_file_target:
            decrypted_file_target.write(decrypted_data)
    
    os.remove(encrypted_file)
    print(f"Decoded: {decrypted_file}")

print("Decode process completed.")
        