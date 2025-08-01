import random
import string

def generate_password(length: int) -> str:
    if length < 4:
        raise ValueError("Password length should be at least 4 to include all character types.")

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure at least one character from each type
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols),
    ]

    # Fill the rest with random characters from all types
    all_chars = lower + upper + digits + symbols
    password += random.choices(all_chars, k=length - 4)

    # Shuffle to avoid predictable order
    random.shuffle(password)

    return ''.join(password)

if __name__ == "__main__":
    try:
        user_input = input("Enter desired password length: ")
        length = int(user_input)
        password = generate_password(length)
        print("Generated password:", password)
    except ValueError as e:
        print("Error:", e)

