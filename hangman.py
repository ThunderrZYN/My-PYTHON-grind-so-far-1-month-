#-=-=-=-=-=-=-=-=---=-=--=-=-=-=-=-=-=-=-=-=-=-=-
#HANGMAN GAME PYTHON PRACTICE
#-=-==-=-=-=---=-==-=-=--=-=-===-=-=-=---=-=----==-
# Easy words (Common, shorter words with clear vowel patterns)

import random

easy_words = [
    "fox",
    "sun",
    "map",
    "frog",
    "camp",
    "king",
    "lamp",
    "wind",
    "shark",
    "plane",
    "ghost",
    "grape",
    "brick"
]

# Hard words (A bit longer, slightly trickier spelling)
hard_words = [
    "adventure",
    "astronaut",
    "calculator",
    "dinosaur",
    "horizon",
    "juicy",
    "mystery",
    "phantom",
    "pyramid",
    "volcano"
]
#difficulty selector function
def difficulty():
    print("""PLAYING HANGMAN
          made by THUNDERR(dev)""")
    while True:
        ez_or_hard = input("easy or hard: ").upper()
        if ez_or_hard == "EASY":
            print(f"selected {ez_or_hard} mode")
            word_sec = random.choice(easy_words)
            game_main(word_sec)
            break
        elif ez_or_hard == "HARD":
            print(f"selected {ez_or_hard} mode")
            word_sec = random.choice(hard_words)
            game_main(word_sec)
            break
        else:
            print("INVALID INPUT:enter easy or hard")
            continue
#main game loop
def game_main(word_sec):
    lives = 6
    guessed_letters = []
    blks = ["_"] * len(word_sec)
    
    while lives > 0:
        if blks == list(word_sec):
            print(f"you win! The word was '{word_sec}'")
            exit()
        print('\nWORD: '+" ".join(blks))
        print(f"you have {lives} lives remaining")
        guess = input("enter your guess: ")
        if len(guess) != 1 or not guess.isalpha():
            print("INVALID INPUT: please enter a single LETTER")
            continue
        elif guess in guessed_letters:
            print("you already guessed that letter")
            continue
        guessed_letters.append(guess)
        if guess in word_sec:
            print("you guessed a letter right!")
            
            for i in range(len(word_sec)):
                if word_sec[i] == guess:
                    blks[i] = guess

        else:
            print("wrong guess!")
            lives -= 1
    print(f"""GAME OVER!! 
          The word was '{word_sec}'""")
    quit()

#calling game
difficulty()