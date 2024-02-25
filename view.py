def get_user_name():
     while True:
        user_name = input("Enter your name: ")
        if user_name.isalpha():
            return user_name
        else:
            print("Invalid input. Please enter a name using only Latin letters.")
            
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
