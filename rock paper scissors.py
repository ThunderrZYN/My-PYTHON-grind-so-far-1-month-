#ROCK-PAPER-SCISSOR GAME MAKING PYTHON PRACTICE
print("WELCOME TO ROCK-PAPER-SCISSORS\nDO YOU WANNA PLAY??\n1.yes\n2.no")

import random

while 1 == 1:   
 #asking to play game   

    try:
        consent = int(input("enter-> "))
    except ValueError:
        print("enter num u dipshit")
        continue
    if (consent > 2) or (consent < 1):
        print("1 or 2 bro")
        continue
    elif consent == 2:
        print("you quitted the game")
        break
    
    #GAME PART
    else:
        rps = ("rock","paper","scissors") 
        p = input("rock,paper or scissors OR quit -> ")#taking input of options
        if p.lower() == "quit":#to quit game
            break
        
        elif p.lower() not in rps:
            print("enter rock or paper or scissors")#bug check
            continue
        else:
            cc = random.choice(rps)
            if p.lower() == "rock" and cc == "scissors" or p.lower() == "paper" and cc == "rock" or p.lower() == "scissors" and cc == "paper":
                print(f"u win {p.lower()} beats {cc}")
                break
            elif p.lower() == cc:
                print(f"{p.lower()} draws against {cc}")
                continue
            else:
                print(f"try again {cc} beats {p.lower()}")
                continue