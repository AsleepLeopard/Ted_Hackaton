import string
import random

def get_sequence(n: int):
    return "".join(random.choices(string.ascii_lowercase, k=n))

if __name__ == "__main__":
    domain = input("Domain: ")
    username = get_sequence(n=8)
    email = f"{username}@{domain}"
    print(email)
