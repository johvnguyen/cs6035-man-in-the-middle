# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: flag4.py
# Bytecode version: 3.9.0beta5 (3425)
# Source timestamp: 2025-04-16 23:13:47 UTC (1744845227)

import hashlib

def obscure_input(input_value):
    encoded_input = input_value.encode()
    return hashlib.sha256(encoded_input).hexdigest()

def obscure_constant():
    secret_key = b'_CS6035-nOva-Fl4G_'
    return hashlib.sha256(secret_key).hexdigest()

def combine_hashes(hash1, hash2):
    return ''.join([hash1[i] if i % 2 == 0 else hash2[i] for i in range(len(hash1))])

def main():
    print('==== You found Flag 4! ====')
    u_input = input('Enter your GTID : ').strip()
    if not u_input:
        print('Error: GTID cannot be empty.')
        return
    first_hash = obscure_input(u_input)
    second_hash = obscure_constant()
    combined = combine_hashes(first_hash, second_hash)
    print('Combined hash   :  ', combined)
if __name__ == '__main__':
    main()