import random

print("WELCOME TO ROCK-PAPER-SCISSORS\nDO YOU WANNA PLAY??\n1. yes\n2. no")

while True:   
    # 1. Entry Check
    try:
        consent = int(input("\nenter-> "))
    except ValueError:
        print("Please enter a valid number (1 or 2), not letters!")
        continue

    if (consent > 2) or (consent < 1):
        print("1 or 2 bro")
        continue
    elif consent == 2:
        print("you quitted the game")
        break
    
    # 2. Player Turn
    rps = ("rock", "paper", "scissors") 
    p = input("rock, paper, scissors OR quit -> ").strip().lower()

    if p == "quit":
        print("you quitted the game")
        break
    
    if p not in rps:
        print("enter rock or paper or scissors")
        continue
        
    # 3. Bot Turn & Matchup Display
    cc = random.choice(rps)
    print(f"\nMatchup: YOU [{p}]  VS  BOT [{cc}]")  # <--- THIS SHOWS THE BOT'S SELECTION
    print("-" * 30)
    
    # 4. Deciding the Winner
    if p == cc:
        print(f"Result: Draw! Play again!\n")
        continue
        
    player_wins = (
        (p == "rock" and cc == "scissors") or 
        (p == "paper" and cc == "rock") or 
        (p == "scissors" and cc == "paper")
    )
    
    if player_wins:
        print(f"Result: You win! {p} beats {cc}\n")
        break
    else:
        print(f"Result: You lose! {cc} beats {p}\n")