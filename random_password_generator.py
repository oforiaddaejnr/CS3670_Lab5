import random
import string

def generate_password(length: int) -> str:
    if length < 4:
        raise ValueError("Password length should be at least 4 to include all character types.")

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols),
    ]

    all_chars = lower + upper + digits + symbols
    password += random.choices(all_chars, k=length - 4)

    random.shuffle(password)

    return ''.join(password)

print(generate_password(12))
