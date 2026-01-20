import random

# List of predefined words
words = ["python", "coding", "hangman", "program", "computer"]

# Choose a random word
secret_word = random.choice(words)

# Create a list to store guessed letters
guessed_letters = []

# Number of allowed incorrect guesses
max_attempts = 6
attempts_left = max_attempts

print("🎮 Welcome to Hangman Game!")
print("Guess the word one letter at a time.")

# Game loop
while attempts_left > 0:
    # Display the current state of the word
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print("\nWord:", display_word)
    print("Attempts left:", attempts_left)

    # Check if the player has won
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word correctly.")
        break

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    # Add guess to guessed letters
    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in secret_word:
        print("✅ Good guess!")
    else:
        print("❌ Wrong guess!")
        attempts_left -= 1

# If attempts are over
if attempts_left == 0:
    print("\n💀 Game Over! You ran out of attempts.")
    print("The word was:", secret_word)