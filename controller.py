import random
from model import caesar_cipher
from view import display_encrypted_name, get_user_name, guess_shift, display_guess_result
from config import CypherConfig
from logger import logger

def start_cypher(config):
    user_name = get_user_name()
    logger.info(f"User name: {user_name}")

    shift_amount = random.randint(config.min_shift, config.max_shift)
    logger.info(f"Shift amount: {shift_amount}")

    encrypted_name = caesar_cipher(user_name, shift_amount)
    display_encrypted_name(encrypted_name)

    correct_guess = False
    attempts = 0
    while not correct_guess:
        user_guess = guess_shift()
        if user_guess == 'q':
            break
        attempts += 1
        logger.info(f"User guess: {user_guess}")
        guessed_name = caesar_cipher(user_name, user_guess)

        if user_guess == shift_amount:
            correct_guess = True
            display_guess_result(True, attempts, user_name)
            logger.info(f"Correct guess in {attempts} attempts")
        else:
            display_guess_result(False, attempts, guessed_name)
            logger.info(f"Incorrect guess: {user_guess}")