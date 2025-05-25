import random

# Predefined list of 5 words
words = ["apple", "banana", "grape", "orange", "mango"]

# Choose a random word from the list
word_to_guess = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

# Display word with underscores
def get_display_word(word, guessed):
    return ''.join([letter if letter in guessed else '_' for letter in word])

# Game loop
print("Welcome to Hangman!")
while incorrect_guesses < max_guesses:
    display_word = get_display_word(word_to_guess, guessed_letters)
    print("\nWord:", display_word)
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("Good guess!")
    else:
        incorrect_guesses += 1
        print(f"Wrong guess! You have {max_guesses - incorrect_guesses} guesses left.")

    if all(letter in guessed_letters for letter in word_to_guess):
        print("\nCongratulations! You guessed the word:", word_to_guess)
        break
else:
    print("\nGame Over! The word was:", word_to_guess)
