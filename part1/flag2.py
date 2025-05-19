# MITM Project - New Flag2
#
# Author: Joseph Abel, Renan Mathias Fernandes
# Email:  jabel9@gatech.edu, renanfernandes@gatech.edu
#
# Generate a unique hash (SHA-256) given a GTID and display it on the screen.

import hashlib


def generate_hash(gtid):
    """Generates a combined SHA-256 hash based on GTID and a secret string."""
    # Hash the provided GTID
    gtid_hash = hashlib.sha256(gtid.encode()).hexdigest()
    # Hash the fixed secret string
    secret_hash = hashlib.sha256(b"_CS6035-FL2025-SMM-").hexdigest()
    # Combine both hashes
    return gtid_hash + secret_hash


def main():
    """Main function to run the script."""
    print("==== You found Flag 2! ====")
    # Prompt the user for their GTID
    gtid = input("Enter your GTID: ").strip()
    
    # Validate GTID input
    if not gtid:
        print("Error: GTID cannot be empty. Please try again.")
        return
    
    # Generate the hash
    final_hash = generate_hash(gtid)
    # Display the hash
    print("\nYour hash is:", final_hash)


if __name__ == "__main__":
    main()