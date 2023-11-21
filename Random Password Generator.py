#importing the Random for Non repeating
import random
#importing the string for printing
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters)
    for _ in range(length))
    return password

# Generate a password with default length of 8 characters
print(generate_password())

# Generate a password with a specified length
a=int(input("Enter the Length of the password to be generated : "))
print(generate_password(a))
