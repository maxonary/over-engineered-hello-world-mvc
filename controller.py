import random
from model import caesar_cipher
from view import display_encrypted_name, get_user_name, guess_shift, display_guess_result

def start_cypher():
    user_name = get_user_name()
    shift_amount = random.randint(1, 9)
    encrypted_name = caesar_cipher(user_name, shift_amount)
    display_encrypted_name(encrypted_name)

    correct_guess = False
    attempts = 0
    while not correct_guess:
        user_guess = guess_shift()
        attempts += 1
        guessed_name = caesar_cipher(user_name, user_guess)

        if user_guess == shift_amount:
            correct_guess = True
            display_guess_result(True, attempts, user_name)
        else:
            display_guess_result(False, attempts, guessed_name)

