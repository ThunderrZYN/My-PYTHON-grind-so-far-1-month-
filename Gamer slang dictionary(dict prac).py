slang_dict = {
    # Core Gaming Terms
    "afk": "Away From Keyboard; temporarily inactive or not at your screen.",
    "brb": "Be Right Back; stepping away for a short moment.",
    "gtg": "Got To Go; leaving the game or stepping off.",
    "gg": "Good Game; typed at the end of a match as sportsmanship.",
    "ez": "Easy; used to taunt the opposing team after a win.",
    "glhf": "Good Luck, Have Fun; said before a match starts.",
    "wp": "Well Played; acknowledging a great move or game by someone.",
    "ff": "Forfeit / Surrender; voting to end a match early when losing badly.",
    
    # Gameplay & Mechanics
    "buff": "An update or change that makes a character, weapon, or ability stronger.",
    "nerf": "A change that weakens a character, weapon, or ability for balance.",
    "grind": "Repeating tasks or fighting enemies over and over to gain XP or items.",
    "rng": "Random Number Generation; absolute luck or randomness in game drops.",
    "clutch": "Winning a round or making a massive play under high pressure.",
    "choke": "Failing or messing up a play right when victory was guaranteed.",
    "aggro": "Drawing enemy aggression or focus onto yourself.",
    "aoe": "Area of Effect; attacks or spells that cover an entire region.",
    "dps": "Damage Per Second; measuring raw damage output, or referring to damage roles.",
    "kdr": "Kill-Death Ratio; total kills divided by total deaths.",
    "meta": "Most Effective Tactic Available; the current strongest strategy or build.",
    "pog": "Play Of the Game; used to react to an incredible play or moment.",
    "smurf": "A high-ranked skilled player using a low-level alt account to dominate beginners.",
    "sweat": "A player trying ridiculously hard in a casual or non-competitive game.",
    
    # Character & Player Types
    "noob": "Beginner or new player who doesn't know how to play well yet.",
    "pro": "Professional player; someone highly skilled at the game.",
    "gng": "Gang; modern substitute for the word 'bro' or team.",
    "op": "Overpowered; something way too strong compared to everything else.",
    "npc": "Non-Player Character; an automated character, or someone who acts like a bot.",
    "camper": "A player who hides in one spot the entire game waiting for easy kills.",
    "toxic": "A player who is mean, hostile, or trash-talks their own team.",
    "feed": "Dying repeatedly to the enemy team, making them stronger."
}
while True:
    word = input("what gamer slang do u wanna know the meaning of: ").strip()
    lower_word = word.lower()  
    if lower_word == "quit":
        print("closed slang dictionary 5000")
        break
    elif lower_word in slang_dict:
        print(lower_word,":",slang_dict[lower_word])
    else:
        print("do u wanna add a slang to the gamer slang dictionary?")
        add_no = input("yes/no: ").lower().strip()
        if add_no == "yes":
            added_word = input("what word do u wanna add: ").strip().lower()
            print("add meaning")
            added_meaning = input(f"{added_word}: ").lower().capitalize()
            slang_dict[added_word] = added_meaning
        elif add_no == "no":
            print("ok,closed slang dictionary 5000")
            break
        else:
            print("invalid input")
            continue
        