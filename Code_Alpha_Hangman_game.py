import random

words = ["banana", "catfish", "iphone", "burger", "zebra"]
word = random.choice(words)

guessed = []
wrong = 0
no_wrong = 6

hangman = [
    " +---+\n     |\n     |\n     |\n  =======",
    " +---+\n O   |\n     |\n     |\n  =======",
    " +---+\n O   |\n |   |\n     |\n  =======",
    " +---+\n O   |\n/|   |\n     |\n  =======",
    " +---+\n O   |\n/|\\  |\n     |\n  =======",
    " +---+\n O   |\n/|\\  |\n/    |\n  =======",
    " +---+\n O   |\n/|\\  |\n/ \\  |\n  ======="
]

while wrong < no_wrong:
    print(hangman[wrong])

    for letter in word:
        if letter in guessed:
            print(letter, end=" ")
        else:
            print("_", end=" ")

    print()

    if all(letter in guessed for letter in word):
        print("\nYou won!")
        break

    guess = input("\nGuess a letter: ").lower()

    if guess in guessed:
        print("\nAlready guessed!")
    elif guess in word:
        guessed.append(guess)
        print("\nCorrect guess!")
    else:
        wrong += 1
        guessed.append(guess)
        print("\nWrong guess! Attempts left:", no_wrong - wrong)

if wrong == no_wrong:
    print(hangman[wrong])
    print("\nYou lost! The word was:", word)