import hashlib


def generate_hash(gtid):
   # Generates a combined SHA-256 hash based on GTID and a secret string
   gtid_hash = hashlib.sha256(gtid.encode()).hexdigest()
   secret_hash = hashlib.sha256(b"CS6035-SU2025-BY5").hexdigest()
   return gtid_hash + secret_hash


def main():
   print("==== You found Flag 5.3! ====")
   gtid = input("Enter your GTID: ").strip()
   if not gtid:
       print("Error: GTID cannot be empty. Please try again.")
       return
   final_hash = generate_hash(gtid)
   print("Your hash is:", final_hash)


if __name__ == "__main__":
   main()