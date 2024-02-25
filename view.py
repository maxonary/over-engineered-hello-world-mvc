def get_user_name():
    return input("Enter your name: ")

def display_encrypted_name(name):
    print(f"Encrypted Name: {name}")

def guess_shift():
    user_input = input("Guess the shift amount (1-9) or 'q' to quit: ")
    if user_input.lower() == 'q':
        return 'q'
    elif user_input.isdigit() and 1 <= int(user_input) <= 9:
        return int(user_input)
    else:
        print("Invalid input. Please enter a valid number between 1 and 9 or 'q' to quit.")
        return guess_shift()

def display_guess_result(correct, attempts, name):
    if correct:
        print(f"Hello {name}! \n You've guessed the correct shift amount in {attempts} attempts!")
    else:
        print(f"Current guess: {name}, \n Try again!")
