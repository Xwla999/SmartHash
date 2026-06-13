import hashlib
from pathlib import Path

def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while chunk := file.read(8192):
            sha256.update(chunk)

    return sha256.hexdigest()

print("SmartHash v1.0")

path = input("Enter file path: ")

if Path(path).exists():
    print("\nSHA256:")
    print(calculate_hash(path))
else:
    print("File not found.")
