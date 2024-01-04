import random

def guess_the_number():
    print("Welcome to the Guess the Number Game!")
    print("I have selected a random number between 1 and 100. Can you guess it?")

    # Generate a random number between 1 and 100
    secret_number=random.randint(1, 100)

    attempts=0

    while True:
        # Get user input for the guess
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts+=1

        # Check if the guess is correct
        if guess==secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
        elif guess<secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if __name__=="__main__":
    guess_the_number()
