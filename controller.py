from model import caesar_cipher
from view import display_message

def display_encrypted_hello_world():
    message = "Hello World"
    encrypted_message = caesar_cipher(message, 5)  # Number is the shift
    display_message(encrypted_message)
