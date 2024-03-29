#Task 3 : Random Password Generator
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation #(Take desired length of password from user)

    # Check if the length is valid
    if length <= 0:
        return "Password length must be greater than 0."

    # Generate the password by selecting random characters from the character set
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

if __name__ == "__main__":
    try:
        password_length = int(input("Enter the desired password length: "))
        password = generate_password(password_length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number for password length.")