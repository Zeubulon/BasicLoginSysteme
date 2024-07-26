import hashlib
import os

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def read_credentials():
    credentials = {}
    if os.path.exists('credentials.txt'):
        with open('credentials.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                username, password = line.strip().split(':')
                credentials[username] = password
    return credentials

def write_credentials(username, password):
    with open('credentials.txt', 'a') as f:
        f.write(f"{username}:{hash_password(password)}\n")

def login(username, password):
    credentials = read_credentials()
    hashed_password = hash_password(password)
    return credentials.get(username) == hashed_password

def register(username, password):
    credentials = read_credentials()
    if username in credentials:
        return False
    write_credentials(username, password)
    return True