#HANGMAN IS A GAME SELECTS WORDS FROM A LIST,DISPLAYS AS UNDERSCORE WHICH REPRESENTS LETTER AND PROMPT
# USER UNTIL THRY EITHER GUESS LETTERS UNTIL THEY EITHER GUESS THE WORD OR RAN OUT OF ATTEMPTS



import random
from words import word_list


def get_word():
    word = random.choice(word_list)
    return word.upper()                   #which used to return a random word from word_list


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:                             #while not =while false
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():                  #1 if user input a letter
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)           #all the indices occurs in a word
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:                          # numerate used to track the no of iteration function
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)        # convert it back to string
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():      #if user input the word
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:                                               #if user input otherthan words\letters
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/                       # double back slash means single slashrepresent escape character
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():                                                # play again input prompting play again
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
