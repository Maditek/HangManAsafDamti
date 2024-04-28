import random
import string
import os
HANGMAN_ASCII_ART = """Welcome to the game Hangman
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
"""

HANGMAN_PHOTOS = {
    0: """x-------x""",
    1: """
    x-------x
    |
    |
    |
    |
    |""",
    2: """
    x-------x
    |       |
    |       0
    |
    |
    |""",
    3: """
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """,
    4: f"""
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |

  """,
    5:
        f"""
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
    """,
    6: f"""
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
  """
}


def is_valid_input(letter_guessed, old_letters_guessed):
    '''return true if the input is 1 letter in the alphabet
     of the english letters and wasn't guessed before, otherwise return false'''
    return len(letter_guessed) == 1 and letter_guessed.isalpha() and letter_guessed.lower() not in old_letters_guessed


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    '''updates old_letters_guessed with letter_guessed if
    it is a valid input otherwise prints a message and returns false'''
    if is_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    print("X")

    sorted_list = sorted(old_letters_guessed)
    formatted_list = ' -> '.join(map(str, sorted_list))
    print(formatted_list)
    return False


def show_hidden_word(secret_word, old_letters_guessed):
    '''prints the parts of the word we already guessed'''
    for i in secret_word:
        if i in old_letters_guessed:
            print(i, end=" ")
        else:
            print("_", end=" ")


def check_win(secret_word, old_letters_guessed):
    '''returns true if all the letters in secret_word are in old_letters_guessed
    otherwise false'''
    for i in secret_word:
        if i not in old_letters_guessed:
            return False
    return True


def print_hangman(num_of_tries):
    '''prints hangman dicitonary at num_of_tries key'''
    print(HANGMAN_PHOTOS[num_of_tries])


def choose_word(file_path, index):
    '''chooses a word in the index thats given from the file given
    also checks if the file exists and if the index is valid'''
    if not os.path.exists(file_path):
        print("File path is not valid.")
        return None
    if index < 0:
        print("Index cannot be negative.")
        return None
    unique_words = []
    all_words = []
    with open(file_path, "r") as words:
        for line in words:
            for word in line.split():
                all_words.append(word)
                if word not in unique_words:
                    unique_words.append(word)
    cyclic_index = (index - 1) % len(all_words)
    return all_words[cyclic_index]


def main():
    MAX_TRIES = 6
    current_tries = 0
    old_letter_guessed = []
    print(HANGMAN_ASCII_ART, "\n", MAX_TRIES)
    file_path = input("enter the file path for the words file")
    index = int(input("Enter the index of the word you want to guess"))
    chosen_word = choose_word(file_path, index)
    if chosen_word is None:
        exit(1)
    print("Let's start")
    print_hangman(current_tries)
    chosen_word_len = len(chosen_word)
    print("_ " * chosen_word_len)
    while current_tries < MAX_TRIES and not check_win(chosen_word, old_letter_guessed):

        letter_guessed = input("Guess a letter")
        if try_update_letter_guessed(letter_guessed, old_letter_guessed):
            if letter_guessed.lower() not in chosen_word:
                print(":(")
                current_tries = current_tries + 1
                print_hangman(current_tries)
        show_hidden_word(chosen_word, old_letter_guessed)
        print("")

    if (check_win(chosen_word, old_letter_guessed)):
        print("you Win!!")
    else:
        print("Better luck next time, you lost!")


if __name__ == "__main__":
    main()
