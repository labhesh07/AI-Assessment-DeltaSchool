import random

def guess_number_game():
    print("Welcome to Guess the Number game!")
    print("I have chosen a number between 1 and 100. You have to guess it.")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        # Prompt the user to guess the number
        guess = int(input("Guess the number between 1 and 100: "))
        attempts += 1

        # Check if the guess is correct, too high, or too low
        if guess < secret_number:
            print("Its low  ! Try again.")
        elif guess > secret_number:
            print("Its high ! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
            break

# Run the game
guess_number_game()
