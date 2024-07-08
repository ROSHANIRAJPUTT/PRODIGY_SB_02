import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0

    print("Welcome to the number guessing game!")
    print("I have selected a number between 1 and 100.")
    
    # Loop until the user guesses the correct number
    while guess != number_to_guess:
        # Prompt the user to input their guess
        try:
            guess = int(input("Please enter your guess: "))
            attempts += 1

            # Provide feedback on the guess
            if guess < number_to_guess:
                print("Your guess is too low. Try again.")
            elif guess > number_to_guess:
                print("Your guess is too high. Try again.")
            else:
                print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Run the game
guess_the_number()
