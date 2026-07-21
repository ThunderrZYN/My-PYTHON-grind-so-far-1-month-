import random
a = random.randint(1 , 100)# getting the random number
i = 0#tries counter
while True:
   
    b = int(input("guess the number: "))

    i += 1
    
    #error fixing
    if b < 1:
        print("num must be range 1 : 100")
        continue
    elif b > 100:
        print("num must be in range 1 : 100")
        continue
    elif b > a:
        print("lower")
        continue
    elif b < a:
        print("higher")
        continue
    else:
        print(f"you win!! it took you {i} tries")
        
        break
