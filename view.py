def get_user_name():
    return input("Enter your name: ")

def display_encrypted_name(name):
    print(f"Encrypted Name: {name}")

def guess_shift():
    return int(input("Guess the shift amount (1-9): "))

def display_guess_result(correct, attempts, name):
    if correct:
        print(f"Hello {name}! \n You've guessed the correct shift amount in {attempts} attempts!")
    else:
        print(f"Current guess: {name}, \n Try again!")
