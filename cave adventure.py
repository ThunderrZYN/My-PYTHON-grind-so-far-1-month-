#CHOOSE YOUR ADVENTURE GAME(USER'S CAVE ADVENTURE)
#FUNCTIONS
#==================================================================================================

#to play again
def play_again():
    
    while True:

       again =input("do you wanna play again(yes/no): ").lower()
       if again == "yes":
           start_game()
       elif again == "no":
           print("Thanks for playing\ncredits: Zayaan(dev)")
           exit()
       else:
           print("enter yes/no")
           continue


#function to get username and ask to play or not
def start_game():
    
    user_name = input("Enter your name: ")
    while True:
    
        print(f"👋 Welcome {user_name} to Zayaan's adventure game!!!")
        play_no = input("Do you wanna play?: ").lower()
        if play_no not in ("yes" , "no"):
            print("Enter yes or no")
            continue
        elif play_no == "no":
            print("You chose to leave the game\n\ngame end")
            break
        else:
            print("u started")
            in_cave(user_name)
            break
   
# game starts with user in a cave            
def in_cave(user_name):
    print(f"\n{user_name} wakes up in a dim,almost fully dark cavern 🌑")
    print(f"\nSound of bats and water dripping is all you can hear\n{user_name} sees two paths\n")
    print("1,A pathway with       2,An opening with sound") 
    print("     light🔦                       coming out🔊" )     
#choice to enter light cave or sound cave    
    while True:
        choice_1 = input("\n\nwhere do you go??(1 or 2): \n")
        if choice_1 not in ("1","2"):
            print("Thats not a choice,you bumped into a wall!! 🤣🤣,\nchoose 1 or 2")
            continue
        elif choice_1 == "1":
            print("you decide to go towards the light🔦")
            towards_light()
            break
        else:
            print("you decide to follow the sound🔊")
            towards_sound()
            break
#function for light choice
def towards_light():
    print("you walk towards the glowing light🔦🔦")
    print("\nYou discover an ancient treasure chest covered in dust..")
    print("\nIt looks valuable 💰")

    while True:   
        
        chest_openo = input("\nDo you open it? 🤔🔐(yes/no): ").lower()
        if chest_openo == "yes":
            print("BEST ENDING:\n\nYOU FIND A TRILLION DOLLA 🤑🤑$$") 
            print("\nyou win🎉🎉")
            play_again()
            break
        elif chest_openo == "no":
            print("CLICK\n\n As you walk a TRAPDOOR OPENS BENEATH UR FEET😱 \nyou fall to death\n\nBAD ENDING")
            play_again()
            break
        else:
            print('invalid response\nenter yes/no')
            continue
#function for sound choice
def towards_sound():
    while True:
        
        feed_or_flight = input("""
                You walk deeper into the dark,echoing shadows.....
                
                Suddenly a MASSIVE,hungry gorilla blocks the path 🦧
                Its stomach growling HARD!!
                
                1,Try to fight the beast   2,give it your food 
                    with your bare hands        from bag 
                
                What do you do?(1 or 2): """)
        if feed_or_flight == "1":
            print("""\n                   You step up to fight the gorilla... ✊💥
                  But the beast is WAY too strong for you!!
                  
                  with one quick swipe,you get knocked out cold.💥
                  
                  ☠️ GAME OVER
                  """)
            play_again()
            break
        elif feed_or_flight == "2":
            print("""You slowly reach into your backpack and toss your food to the gorilla... 🍎
                    The gorilla happily devours the snack and calms down completely. 🦧✨

                    It steps aside, revealing a hidden crack in the cave wall.
                    You squeeze through the gap and find the SECRET EXIT! 🌅

                    You see the sunlight and escape the cave safely!

                    🎉 YOU WIN!""")
            play_again()
            break
        else:
            print("enter 1 or 2")
            continue

#MAIN GAME
start_game()