import random
from words import word_list

def get_word():
    word=random.choice(word_list)
    return word.upper()

def play(word):
    word_comp = '_ ' * len(word)
    guessed= False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("HANGMAN")
    print("LET'S GET STARTED!!")
    print(display_hangman(tries))
    print(word_comp)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Enter your guess letter or word : ").upper()
        if len(guess)==1 and guess.isalpha():
            if guess in guessed_letters:
                print("You have already guessed", guess)
            elif guess not in word:
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Great Job!! "+guess+" is in the word")
                guessed_letters.append(guess)
                word_list = list(word_comp)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_list[index] = guess
                word_comp = "".join(word_list)
                if "_" not in word_comp:
                    guessed = True

        elif len(guess)==len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You have already guessed",guess)
            elif guess != word:
                print(guess," is not the word")
                tries -= 1
                guessed_words.append(guess)
            else:
                guesssed = True
                word_comp = word
            
            

        else:
            print("Oops!! Not a Valid guess.Please enter a valid letter or word")            
        
        print(display_hangman(tries))
        print(word_comp)
        print("\n")
    
    if guessed:
        print("Congrats!! You have guessed the word. YOU WIN ")
    else:
        print("Oops! Sorry you have ran of tries. The Word was "+word+" Better Luck Next Time.")

def display_hangman(tries):
    stages = ["""
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / \\
                -
                """,
                """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     /
                -
                """,
                """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |
                -
                """,
                """
                --------
                |      |
                |      O
                |     \\|
                |      |
                |
                -
                """,
                """
                --------
                |      |
                |      O
                |      |
                |      |
                |
                -
                """,
                """
                --------
                |      |
                |      O
                |
                |
                |
                -
                """,
                """
                --------
                |      |
                |
                |
                |
                |
                -
                """   ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("Wanna Play Again?(Y/N) : ").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()

