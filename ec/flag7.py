# MITM Project - New Flag7
#
# Author: Joseph Abel and Renan Fernandes
# Email:  jabel9@gatech.edu, renanfernandes@gatech.edu
#
# Generate a unique hash (sha256) given a gtID and display on the screen.
# DO NOT MODIFY THIS CODE

import hashlib

def obscure_input(input_value):
    encoded_input = input_value.encode()
    return hashlib.sha256(encoded_input).hexdigest()

def obscure_constant():
    secret_key = b"_CS6035-Kust0-Qu3rYL33t"
    return hashlib.sha256(secret_key).hexdigest()

def combine_hashes(hash1, hash2):
    return ''.join([hash1[i] if i % 2 == 0 else hash2[i] for i in range(len(hash1))])

def main():
    print("==== You found Flag 7! ====")
    
    # Input prompt for GTID
    u_input = input("Enter your GTID : ").strip()

    if not u_input:
        print("Error: GTID cannot be empty.")
        return

    # Obfuscated hash generation
    first_hash = obscure_input(u_input)
    second_hash = obscure_constant()
    combined = combine_hashes(first_hash, second_hash)

    # Displaying the final combined hash
    print("Combined hash   :  ", combined)

if __name__ == "__main__":
    main()