import random
from words import words  # this is importing from words.py that is in the folder
word = random.choice(words)
word = word.upper()
word_letter = set(word)
correct_guess = set()
# built by Pyi Ent Kyaw


def hangman():
    user_guess = input("Type an alphabet:")
    user_guess = user_guess.upper()
    if user_guess in word_letter:
        if user_guess not in correct_guess:
            print("You guess correctly.")
            correct_guess.add(user_guess)
        else:
            print("You have already guess this.")
    elif (user_guess == 'SCORE'):  # these are easter eggs
        print(f"{correct_guess}")
    elif (user_guess == 'HACK'):  # easter eggs also useful for testing
        print(f"{word}")
    else:
        print("You guess wrong!")


mode = input("'n' for normal,'h' for hard:")
if mode == 'n':
    while True:
        hangman()
        if correct_guess == word_letter:
            print(f"You have win the game.The word was {word}")
            break
elif mode == 'h':
    error_count = 0
    while True:
        hangman()
        if correct_guess == word_letter:
            print(f"You have win the game.The word was {word}")
            break
        else:
            error_count += 1
            if error_count >= 10:
                print(f"Sorry! You lost!\n The word was {word}")
                print(f"Your guess were {correct_guess}")
                break
