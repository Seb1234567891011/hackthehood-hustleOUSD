#Guessing game - Sebastian, Gabe, Jessie
import random 
def generate_random_number():
    """Generates a random number between 1 and 100 inclusive."""
    return random.randint(1, 100)
def get_user_guess():
    """
    Prompts the user for a guess and validates the input.
    Ensures the guess is an integer between 1 and 100.
    Returns the valid guess.
    """
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
  else:
                print("❗ Please enter a number between 1 and 100.")
        except ValueError:
            print("❗ Invalid input. Please enter a whole number.")
            def play_guessing_game():
    """
    Main game logic.
    Generates a secret number and lets the user guess until they get it right.
    Tracks number of attempts and gives feedback.
    """
    secret_number = generate_random_number()
    attempts = 0

    print("\n🎯 I'm thinking of a number between 1 and 100. Can you guess it?")

    while True:
        guess = get_user_guess()
        attempts += 1

        if guess < secret_number:
            print("🔻 Too low! Try again.\n")
        elif guess > secret_number:
            print("🔺 Too high! Try again.\n")
        else:
            print(f"✅ Correct! You guessed the number in {attempts} attempts.\n")
            break
            def game_loop():
    """
    Keeps the guessing game running until the user chooses to stop.
    """
    while True:
        play_guessing_game()
        play_again = input("🔁 Would you like to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("👋 Thanks for playing! Goodbye.")
            break
            if __name__ == "__main__":
    game_loop()