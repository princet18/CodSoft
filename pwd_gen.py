import random
import string


def generate_password(length, include_uppercase=True, include_digits=True, include_special_chars=True):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def register_user(username, password):
    # Placeholder function to simulate user registration
    print(f"User '{username}' registered with password: {password}")


def main():
    print("Welcome to the User Registration System!")

    username = input("Enter your username: ")

    length = int(input("Enter the desired length of the password: "))
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, include_uppercase, include_digits, include_special_chars)

    register_user(username, password)
    print("User registration successful!")


if __name__ == "__main__":
    main()
