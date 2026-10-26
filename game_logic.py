import random
# Import the snowman graphics from the ascii file
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])

    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def play_game():
    # Outer loop to handle the replay functionality
    while True:
        secret_word = get_random_word()
        guessed_letters = []
        mistakes = 0
        # The maximum number of mistakes depends on the number of the stages
        # (STAGES length - 1, i.e. 3)
        max_mistakes = len(STAGES) - 1

        print("Welcome to Snowman Meltdown!")

        # The game loop: it iterates until there are not too many mistakes
        # and there are still letters to guess
        while mistakes < max_mistakes:
            display_game_state(mistakes, secret_word, guessed_letters)

            # --- INPUT VALIDATION ---
            # Loop until the user provides a single valid alphabetical character
            while True:
                guess = input("Guess a letter: ").lower()

                if len(guess) != 1:
                    print("Please enter exactly ONE letter!")
                elif not guess.isalpha():
                    print("Please enter a valid alphabetical character (a-z)!")
                elif guess in guessed_letters:
                    print("You have already guessed that letter! Try another one.")
                else:
                    break  # Valid input received, exit the input validation loop

            # Save the valid guess to the list of guessed letters
            guessed_letters.append(guess)

            # Check if the guessed letter is contained in the word
            if guess in secret_word:
                print("Good guess!")
            else:
                print("Incorrect guess!")
                mistakes += 1

            # Check if all letters have been guessed
            won = True
            for letter in secret_word:
                if letter not in guessed_letters:
                    won = False
                    break

            if won:
                # If succeeded, the actual stage is displayed and exit the loop
                display_game_state(mistakes, secret_word, guessed_letters)
                print("Congratulations, you saved the snowman!")
                break  # Exit the inner game loop

        # If the loop ended and the maximum mistakes reached, the snowman has melted
        if mistakes == max_mistakes:
            display_game_state(mistakes, secret_word, guessed_letters)
            print("Game Over! The snowman melted. The word was: " + secret_word)

        # --- REPLAY OPTION ---
        # Ask the user if they want to start a new game
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again != "yes" and play_again != "y":
            print("Thanks for playing! Goodbye.")
            break  # Exit the outer loop, terminating the program


if __name__ == "__main__":
    play_game()
