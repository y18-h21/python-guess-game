import random

def number_guessing_game():
    """
    A simple number guessing game where the player tries to guess a random number.
    """
    lower_bound = 1  # You can change the lower bound
    upper_bound = 100  # You can change the upper bound

    while True:
        secret_number = random.randint(lower_bound, upper_bound)
        print(f"Welcome to the Number Guessing Game!")
        print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")

        # 2. User Guesses
        attempts = 0
        while True:
            try:
                guess = int(input("Enter your guess: "))
                attempts += 1
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            # 3. Feedback
            if guess < secret_number:
                print("Too low! Try guessing higher.")
            elif guess > secret_number:
                print("Too high! Try guessing lower.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break

        # 4. Ask if they want to play again
        play_again = input("Would you like to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    number_guessing_game()
